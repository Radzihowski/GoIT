import mimetypes
import pathlib
import socket
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

UDP_IP = '127.0.0.1'
UDP_PORT = 5000

class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        print(pr_url)
        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/message':
            self.send_html_file('message.html')
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()
            else:
                self.send_html_file('error.html', 404)

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_data(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server = UDP_IP, UDP_PORT
        sock.sendto(data, server)
        print(f'Send data: {data.decode()} to server: {server}')
        sock.close()

    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        print(data)
        self.send_data(data)
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        with open(f'.{self.path}', 'rb') as file:
            self.wfile.write(file.read())

def run(server_class=HTTPServer, handler_class=HttpHandler):
    print("run server")
    server_address = ('', 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    run()
