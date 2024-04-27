# Створення Decimal з дійсних чисел

from decimal import Decimal
num_one = 1.37
num_two = 1.5
print(num_one)

first = Decimal(num_one)
print(first)

first = Decimal.from_float(num_one)
print(first)


second = Decimal.from_float(num_two)
print(second)


# using str
num_one = 1.37
num_two = 1.5
print(num_one)

first = Decimal(str(num_one))
print(first)

second = Decimal(str(num_two))
print(second)