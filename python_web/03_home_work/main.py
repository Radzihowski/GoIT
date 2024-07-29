import shutil
from pathlib import Path
import os

BASE_DIR = Path(__file__).parent.resolve()
print(BASE_DIR)

def file_handler(file: Path, dist: Path):
    ext = file.suffix[1:]
    print(ext)
    target_folder = dist.joinpath(ext)
    print(f"Target folder: {target_folder}")
    if not target_folder.exists():
        os.makedirs(target_folder)
    shutil.copy(file, target_folder)

def folder_handler(folder: Path, dist):
    for file in list(folder.glob("**/*")):
        if file.is_file():
            file_handler(file, dist)
        # else:
        #     folder_handler(file, dist)

def main():

    dist = BASE_DIR.joinpath("dist")
    input_dir = BASE_DIR.joinpath("input")

    for file in input_dir.iterdir():
        if file.is_file():
            file_handler(file, dist)
        else:
            folder_handler(file, dist)



if __name__ == "__main__":
    main()