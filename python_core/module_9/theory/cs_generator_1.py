def first_second_counter():
    while True:
        yield 1
        yield 2

my_generator = first_second_counter()
test = iter([9, 8, 7, 6, 5, 4])

for _ in range(6):
    print(next(my_generator))
