s = b'Hello!'
print(s[4])

byte_string = b'hello world!'
print(byte_string)

byte_str = 'some text'.encode()
print(byte_str)

numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)

some_numbers = bytes([127, 155, 255])
print(some_numbers)

for num in [127, 155, 250, 255]:
    print(hex(num))

print(ord('s'))
print(chr(115))

s = "Привіт!"

utf8 = s.encode()
print(utf8) # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'

utf16 = s.encode('utf-16')
print(utf16)  # b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'

s_from_utf16 = utf16.decode('utf-16')
print(s_from_utf16 == s)  # True

print(b'Hello world!'.decode('utf-16')) # 效汬⁯潷汲Ⅴ

byte_array= bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)