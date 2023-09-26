# ЗАВДАННЯ: КОД ЦЕЗАРЯ

# Тести перевіряють та кодують наступні рядки:
#
# "Hello my little friends!", offset = 37,
# "Hello world!", offset = 7

message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if 'a' <= ch <= 'z':
        pos = (ord(ch) - ord('a'))
        pos = (pos + offset) % 26
        new_char = chr(pos + ord('a'))
        encoded_message = encoded_message + new_char
    elif 'A' <= ch <= 'Z':
        pos = (ord(ch) - ord('A'))
        pos = (pos + offset) % 26
        new_char = chr(pos + ord('A'))
        encoded_message = encoded_message + new_char
    else:
        encoded_message = encoded_message + ch

print(encoded_message)
