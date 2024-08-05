import threading
from main import run
from socket_server import run_server

web_server = threading.Thread(target=run)
socket_server = threading.Thread(target=run_server)

web_server.start()
socket_server.start()
web_server.join()
socket_server.join()
print('Done!')
