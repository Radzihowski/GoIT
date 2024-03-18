import argparse
from pathlib import Path
from shutil import copyfile

output_folder = Path('dist')

def read_folder(path: Path) -> None:
    for element in path.iterdir():
        if element.is_dir():
            read_folder(element)
        else:
            copy_file(element)

def copy_file(file: Path) -> None:
    ext = file.suffix
    new_path = output_folder / ext
    new_path.mkdir(parents=True, exist_ok=True)
    copyfile(file, new_path / file.name)

read_folder(Path('picture'))