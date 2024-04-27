from pathlib import Path

folder = Path('temp')

try:
    with open(folder / 'test.txt', 'r') as f:
        for line in f:
            print(line, end='')
except Exception as e:
    print('Error', e)
finally:
    print('Happy end')