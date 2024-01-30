# Попрацюємо трохи зі специфікацією у форматуванні рядків. Напишіть функцію formatted_numbers, яка повертає список
# відформатованих рядків, щоб під час виведення наступного коду:
#
# for el in formatted_numbers():
#     print(el)
# Виходила наступна таблиця:
#
# | decimal  |   hex    |  binary  |
# |0         |    0     |         0|
# |1         |    1     |         1|
# |2         |    2     |        10|
# |3         |    3     |        11|
# |4         |    4     |       100|
# |5         |    5     |       101|
# |6         |    6     |       110|
# |7         |    7     |       111|
# |8         |    8     |      1000|
# |9         |    9     |      1001|
# |10        |    a     |      1010|
# |11        |    b     |      1011|
# |12        |    c     |      1100|
# |13        |    d     |      1101|
# |14        |    e     |      1110|
# |15        |    f     |      1111|
# всі стовпці мають ширину 10 символів
# у заголовків таблиці вирівнювання по центру
# перший стовпець десяткових чисел — вирівнювання по лівому краю
# другий стовпець шістнадцяткових чисел — вирівнювання по центру
# третій стовпець двійкових чисел — вирівнювання з правого краю
# вертикальний символ | не входить у ширину стовпця
# Як ви вже зрозуміли, функція formatted_numbers виводить таблицю чисел від 0 до 15 у десятковому, шістнадцятковому та
# бінарному форматі.

# Варіант 1
def formated_numbers(digit='a'):
    result = []
    result.append("|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary'))
    try:
        for dig in range(digit + 1):
            result.append("|{:<10d}|{:^10x}|{:>10b}|".format(dig, dig, dig))
    except Exception:
        result.append('не правильний або відсутній аргумент')
    return result


for el in formated_numbers(15):
    print(el)


# Варіант 2
def formated_numbers(digit='a'):
    header = ["|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')]
    result = []
    for i in range(digit + 1):
        result.append("|{0:<10d}|{0:^10x}|{0:>10b}|".format(i))
    return (header + result)


for el in formated_numbers(15):
    print(el)


# Варіант 3
def formated_numbers(digit):
    header = "|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')
    result = []

    result.append(header)

    for i in range(digit + 1):
        decimal = i
        hex_number = hex(i)[2:]
        binary = bin(i)[2:]
        result.append("|{0:<10d}|{0:^10x}|{0:>10b}|".format(decimal, hex_number, binary))
    return result


for el in formated_numbers(15):
    print(el)


# Варіант 4 Це доволі вредне завдання, тут потрібно бути максимально точним. Автоперевірка буде перевіряти лише функцію,
# а твій виклик вона проігнорує, виходить що потрібно задати менш універсальну функцію, яка буде просто виводити числа
# від 0 до 15:
def formatted_numbers():
    header = ["|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')]
    result = []
    for i in range(15 + 1):
        result.append("|{0:<10d}|{0:^10x}|{0:>10b}|".format(i))
    print(header + result)
    return (header + result)
