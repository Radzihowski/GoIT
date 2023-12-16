from pathlib import Path

try:
    tmp = Path('Text.txt')
    tmp.unlink()
except FileNotFoundError:
    pass