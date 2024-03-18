message = "Привіт світ! Hello world!"
print(message.encode())
print(message.encode('utf-16'))
print(message.encode('cp1251'))

with open('utf-8.txt', 'wb') as file:
    file.write(message.encode('utf-8'))

with open('utf-8.txt', 'rb') as file:
    print(file.read().decode('utf-8'))