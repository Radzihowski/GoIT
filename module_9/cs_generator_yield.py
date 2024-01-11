def eight_bit_counter():
    value = 0
    while True:
        yield value
        value += 1

def foo():
    print(123)


my_generator = eight_bit_counter()

print(type(my_generator))
print(type(foo))

for _ in range(6):
    print(next(my_generator))
