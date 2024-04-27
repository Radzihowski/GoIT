# З файлу country.csv отримати словник виду {код_країни: ім'я_країни}

import csv

FILENAME = 'countries.csv'
country_codes = {}

with open(FILENAME) as file:
    reader = csv.reader(file)
    for line in reader:
        country_codes[line[0]] = line[1]
    country_codes.pop('Code')

print(country_codes['AD'])
print(country_codes.get('UA'))