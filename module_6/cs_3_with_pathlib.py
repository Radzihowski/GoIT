# Читаємо файл за допомогою бібліотеки pathlib
#
# За допомогою оператора with. Менше коду та зручність


from pathlib import Path

file_name = Path('./Temp')

try:
    with open(file_name / 'Text.txt', 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end="")
except Exception as e:
    print(f"{e} with file file")