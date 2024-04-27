# Читаємо файл за допомогою бібліотеки pathlib
# Без оператора with. Необхідно закрити файл самому


from pathlib import Path

file_name = Path('../Temp')

try:
    file = open(file_name/'Text.txt', 'r', encoding="utf-8")
    try:
        while True:
            line = file.readline()
            line = line.rstrip()
            if not line:
                break
            print(line)
    except OSError:
        print(f"Error while reading file")
    finally:
        file.close()
except Exception as e:
    print(f"{e} with file file")