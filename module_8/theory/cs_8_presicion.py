from decimal import Decimal, getcontext

value = Decimal('2') / Decimal ('3')
print(value)

print(round(2/3, 5))

getcontext().prec = 6
value_second = Decimal('2') / Decimal ('3')
print(value_second)
