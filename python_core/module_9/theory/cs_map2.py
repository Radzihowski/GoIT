def power(value):
    return pow(value, 2)

squares = list(map(power, [i for i in range(10)]))
print(squares)

squares = list(map(power, range(10)))
print(squares)