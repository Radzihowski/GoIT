from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP

number = Decimal('1.45')
print(number.quantize(Decimal('1.0'), rounding=ROUND_HALF_EVEN))
print(number.quantize(Decimal('1.0'), rounding=ROUND_HALF_UP))
print(Decimal('3.141592653589793').quantize(Decimal('1.00000000000')))