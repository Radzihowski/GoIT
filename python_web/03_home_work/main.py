import shutil
from pathlib import Path
import os
from multiprocessing import Pool

BASE_DIR = Path(__file__).parent.resolve()
print(BASE_DIR)

def file_handler(file_and_dist):
    file, dist = file_and_dist
    ext = file.suffix[1:]  # Get the file extension without the dot
    print(ext)
    target_folder = dist.joinpath(ext)
    print(f"Target folder: {target_folder}")
    if not target_folder.exists():
        target_folder.mkdir(parents=True, exist_ok=True)  # Create target folder if it doesn't exist
    shutil.copy(file, target_folder / file.name)  # Copy the file to the target folder

def folder_handler(folder: Path, dist: Path):
    all_files = [f for f in folder.glob("**/*") if f.is_file()]
    return all_files

def main():
    dist = BASE_DIR.joinpath("dist")
    input_dir = BASE_DIR.joinpath("input")

    if not dist.exists():
        dist.mkdir()

    files_to_handle = []

    for file in input_dir.iterdir():
        if file.is_file():
            files_to_handle.append((file, dist))
        else:
            files_to_handle.extend([(f, dist) for f in folder_handler(file, dist)])

    with Pool(8) as pool:  # Limit the number of parallel processes to 8
        pool.map(file_handler, files_to_handle)

if __name__ == "__main__":
    main()
