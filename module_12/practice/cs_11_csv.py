# Зберегти у файлі таблицю квадратів і кубів цілих чисел від 1 до 20

import csv
from pprint import pprint

FILENAME = 'table.csv'

with open(FILENAME, 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(1, 21):
        writer.writerow([i, pow(i, 2), pow(i, 3)])

with open(FILENAME) as file:
    reader = csv.reader(file)
    result = []
    for line in reader:
        result.append(line)

print(result)
pprint(result)