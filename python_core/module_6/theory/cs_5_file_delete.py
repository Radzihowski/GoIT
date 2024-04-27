from pathlib import Path

try:
    tmp = Path('../text.txt')
    tmp.unlink()
except FileNotFoundError:
    pass