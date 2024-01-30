# Найбільш поширений формат зберігання даних у табличному вигляді. По суті є просто текстовим файлом, де обумовлені
# символи мають значення роздільників. У UNIX прийнято:
#
# \n -- роздільник рядків
# , -- роздільник колонок Не рідко зустрічається \t (символ табуляції) як роздільник колонок.

import csv

with open('names.csv', 'w', newline='\n') as csvfile:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Banana'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Octopus'})
    writer.writerow({'first_name': 'Sad', 'last_name': 'Novelist'})

with open('names.csv') as file:
  print(file.read())