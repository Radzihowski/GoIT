def caching_fibonacci():
    cache = {0: 0, 1: 1, 2: 1}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            return result
        return result
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))
