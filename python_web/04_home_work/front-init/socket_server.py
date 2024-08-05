import json
import socket
import urllib.parse
from datetime import datetime
from pathlib import Path

BASDIR = Path(__file__).parent
UDP_IP = '127.0.0.1'
UDP_PORT = 5000
STORAGE_PATH = BASDIR.joinpath("storage", "data.json")

def save_file_to_json(data: dict):
    if STORAGE_PATH.exists():
        with open(STORAGE_PATH, 'r+') as file:
            file_data = json.load(file)
            file_data.update(data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
    else:
        with open(STORAGE_PATH, 'w') as file:
            json.dump(data, file, indent=4)
    print("Data saved")

def run_server():
    print("Run socket server")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = UDP_IP, UDP_PORT
    sock.bind(server)
    try:
        while True:
            data, address = sock.recvfrom(1024)
            print(f'Received data: {data.decode()} from: {address}')
            data_parse = urllib.parse.unquote_plus(data.decode())
            print(data_parse)
            data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
            print(data_dict)
            current_time = datetime.now()
            extended_dict = {str(current_time): data_dict}
            print(extended_dict)
            save_file_to_json(data=extended_dict)
    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()


if __name__ == '__main__':
    run_server()
