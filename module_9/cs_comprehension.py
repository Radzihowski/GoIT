square_comp = (i ** 2 for i in range(10))
print(square_comp)

for _ in range(11):
    try:
        print(next(square_comp))
    except StopIteration:
        pass