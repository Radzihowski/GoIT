import timeit
from multiprocessing import Pool, cpu_count

def factors(n):
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return sorted(result)

def factorize(*numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(factors, numbers)
    return result


if __name__ == "__main__":
    execution_time = timeit.timeit(lambda: factorize(128, 255, 99999, 10651060), number=1)     # Довелось
    # використовувати timeit() оскільки time() давав стабільно 0


    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    print(f"All tests passed. Execution time: {execution_time} seconds.")