# Запити іншими методами HTTP
#
# Поки що ми виконували тільки GET запити, але документація наводить приклади відправлення для інших методів HTTP:
#
# session.post('http://httpbin.org/post', data=b'data')
# session.put('http://httpbin.org/put', data=b'data')
# session.delete('http://httpbin.org/delete')
# session.head('http://httpbin.org/get')
# session.options('http://httpbin.org/get')
# session.patch('http://httpbin.org/patch', data=b'data')
#
# Розглянемо приклад відправлення POST запиту. Спочатку створимо найпростіший Web-сервер, який прийматиме і надсилатиме
# назад дані POST запиту:
#

from http.server import HTTPServer, BaseHTTPRequestHandler

class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        print(data)
        self.send_response(201)
        self.end_headers()
        self.wfile.write((b'Done request!' + data))

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 5000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()

if __name__ == '__main__':
    run()