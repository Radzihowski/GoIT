import csv

FILENAME = 'users.csv'

users = [
  {'name': 'Roman', 'age': 22, 'sex': 'male'},
  {'name': 'Oksana', 'age': 22, 'sex': 'female'},
  {'name':'Mike', 'age': 22, 'sex': 'male'},
]

with open(FILENAME, 'w', newline='', encoding='utf-8') as file:
    columns = ['name', 'age', 'sex']
    writer = csv.DictWriter(file, delimiter=',', fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)