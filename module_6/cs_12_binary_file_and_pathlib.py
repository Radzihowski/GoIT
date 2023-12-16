# Робота з файлами засобами pathlib
# Бінарний файл

from pathlib import Path

file = Path('test_binary.txt')
file.write_bytes(b"First line 123")
print(file.read_bytes().decode())