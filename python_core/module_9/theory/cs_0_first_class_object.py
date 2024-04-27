# Функця, як об'єкту першого класу
# Сутність, що задовольняє переліченим вище вимогам, називається об'єктом першого класу (або об'єктом першого порядку):
# 1) може бути збережена у змінній або структурі даних;

def sum(a, b):
    return a + b


new_sum = sum
print(new_sum(3, 6))


# 2) може бути передана в іншу функцію як аргумент;

def sum(a, b):
    return a + b


def operation(a, b, func):
    return func(a, b)


print(operation(3, 10, sum))


# 3) може бути повернута з функції як результат;
def sum(a, b):
    return a + b


def minus(a, b):
    return a - b


def power(a):
    return pow(a, 2)

def get_result(operator):
    if operator == '+':
        return sum
    if operator == '-':
        return minus
    if operator == '*':
        return power

sum_func = get_result('+')
print(sum_func(9, 3))

sum_func = get_result('-')
print(sum_func(9, 3))

sum_func = get_result('*')
print(sum_func(9))

# можна викликати через подвійні дужки
print(get_result('*')(10))