# Порахувати суму всіх чисел через рекурсію
def sum_numbers(max_num: int) -> int:
    if max_num <= 0:
        return 0
    if max_num == 1:
        return 1
    return max_num + sum_numbers(max_num - 1)

print(sum_numbers(10))
