from pathlib import Path

folder = Path('../Temp')

message = "Hello, Привіт"

print(message.encode())
print(message.encode('utf-16'))
print(message.encode('cp1251'))

print(b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00\x1f\x04@\x048\x042\x04V\x04B\x04'.decode('utf-16'))
print(b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00\x1f\x04@\x048\x042\x04V\x04B\x04'.decode('cp1251'))

with open(folder/'utf-8.txt', 'wb') as f:
    f.write(message.encode())

with open(folder/'utf-16.txt', 'wb') as f:
    f.write(message.encode('utf-16'))

with open(folder/'cp1251.txt', 'wb') as f:
    f.write(message.encode('cp1251'))

with open(folder/'utf-8.txt', 'rb') as f:
    print(f.read().decode('utf-8'))

with open(folder/'cp1251.txt', 'rb') as f:
    print(f.read().decode('cp1251'))