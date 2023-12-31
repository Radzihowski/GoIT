# Зручно якщо ми розбиваємо на різні списки набори телефонних операторів

from collections import defaultdict

phone_numbers = ['0509993636', '0679993636', '0959993636', '0969993636', '0509993637', '0639993636', '0509993632', '0339993632']

phone_operator_numbers = defaultdict(list)

for ph in phone_numbers:
    if ph.startswith('050') or ph.startswith('095'):
        phone_operator_numbers['Vodafone'].append(ph)
    elif ph.startswith('067') or ph.startswith('096'):
        phone_operator_numbers['Kyivstar'].append(ph)
    elif ph.startswith('063') or ph.startswith('093'):
        phone_operator_numbers['Lifecell'].append(ph)
    else:
        phone_operator_numbers['WTF'].append(ph)

print(phone_operator_numbers)
print(phone_operator_numbers.get('Kyivstar'))
print(phone_operator_numbers.get('Kyivstars'))
print(phone_operator_numbers)