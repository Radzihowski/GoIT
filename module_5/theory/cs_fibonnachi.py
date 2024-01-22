# Good example with cache usage
def fibonnachi(n):
    fib_list = [0, 1]
    if n <= 1:
        return fib_list

    for element in range(2, n + 1):
        fib_number = fib_list[element - 2] + fib_list[element - 1]
        fib_list.append(fib_number)

    return fib_list[n]


# return n if n <= 1 else fibonnachi(n-2) + fibonnachi(n-1)

print(fibonnachi(5))
print(fibonnachi(8))
print(fibonnachi(3))
