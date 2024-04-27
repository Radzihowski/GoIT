import random
import pathlib

corrent_dir = pathlib.Path(__file__).parent

def get_random_joke():
    try:
        with open(corrent_dir / "jokes.txt", 'r', encoding='utf-8') as file:
            jokes = file.readlines()
            return  random.choice(jokes).strip()
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."