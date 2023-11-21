def add(number_one, number_two):
    return number_one + number_two


print(add(2, 5))


def add_all_number(*args):
    sum = 0
    print(type(args))
    for values in args:
        try:
            sum += float(values)
        except ValueError:
            continue
        except TypeError:
            continue
    return sum


print(add_all_number(2, 3, 4, 5, 6, 12, 2.3, 'true', True))
