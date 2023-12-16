# Використання glob

from pathlib import Path

file_name = Path('.')

for elem in file_name.glob('*t*'):
    print(elem)

for elem in file_name.glob('*.txt'):
    print(elem)

for elem in file_name.glob('README*'):
    print(elem)

for elem in file_name.glob('*/'):
    print(elem)