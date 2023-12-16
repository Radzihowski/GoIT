# Робота з файлами засобами pathlib
# Текстовий файл

from pathlib import Path

file = Path('test_file.txt')

file.write_text("First line")
file.write_text("Second line")
file.write_text("Final line")

print(file.read_text())