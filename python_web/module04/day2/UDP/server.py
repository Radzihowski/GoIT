# Сервер:
# 1. Створюємо сокет типу socket.SOCK_DGRAM
# 2. За допомогою методу bind зв'язуємо сокет із адресою служби
# 3. Повторюємо наступні дії у нескінченному циклі:
#   - запит у клієнта сокету даних методом recvfrom (блокуюча операція)
#   - обробка даних
#   - надсилання результату клієнту за допомогою методу sendto

# Наш приклад — звичайний ехо-сервер, який відправляє і отримує одні й ті самі дані на сервер. Сервер відкритий на
# порту 8080 і отримує сокети даних у розмірі 1024 байт.

import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 8080


def run_server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    sock.bind(server)
    try:
        while True:
            data, address = sock.recvfrom(1024)
            print(f'Recived data: {data.decode()} from: {address}')
            sock.sendto(data, address)
            print(f'Send data: {data.decode()} to: {address}')

    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()


if __name__ == '__main__':
    run_server(UDP_IP, UDP_PORT)