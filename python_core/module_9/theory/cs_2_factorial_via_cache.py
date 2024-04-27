# Замикання
# Особливість існування вкладених локальних просторів імен і той факт, що вони створюються динамічно, дає змогу
# використовувати механізм замикань у Python.

def factorial(n, cache={}):
    if n < 0:
        raise ValueError

    def counter(n):
        result = 1
        for value in range(1, n + 1):
            if value in cache:
                result = cache[value]
            else:
                print(result)
                result = value * cache.get(value - 1, 1)
                print(result)
                print(cache)
                cache[value] = result
                print(cache)
                print('{} not in cache {}'.format(value, result))
        return result

    return counter(n)


print(factorial(3))
print(factorial(6))
# print(factorial(4))