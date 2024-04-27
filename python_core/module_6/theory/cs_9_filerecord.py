# Запис в файл

from pathlib import Path

folder = Path('../Temp')

data = ['First line', 'Second line', 'Final line']

#Методи запису даних у файл

# Запис одног рядка ітераційно, тип запису -- перезапис
with open(folder/'data.txt', 'w', encoding="utf-8") as file:
    for line in data:
        file.write(f"{line}\n")
# Запис багатьох рядків за раз, тип запису -- добавлення нових даних в кінець файлу
with open(folder/'data.txt', 'a', encoding="utf-8") as file:
    file.writelines(['First lines\n', 'Second lines\n', 'Final lines\n'])