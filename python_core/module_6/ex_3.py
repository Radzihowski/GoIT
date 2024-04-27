# У попередній задачі ми записали співробітників у файл у такому вигляді:
#
# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19
# Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з файлу та повертатиме список співробітників у вигляді:
#
# ['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
# Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його необхідно прибирати при додаванні прочитаного рядка до списку.
#
# Вимоги:
#
# прочитайте вміст файлу за допомогою режиму "r".
# ми поки що не використовуємо менеджер контексту with
# поверніть із функції список співробітників із файлу
def read_employees_from_file(path):
    file = open(path, 'r')
    my_list = []

    for line in file:
        new_line = line.rstrip()
        my_list.append(new_line)
        print(new_line)
    file.close()
    return my_list


# Мій варіант на якому я готувався
def read_employees_from_file(path):
    file = open('outputex2.txt', 'r')
    my_list = []

    for line in file:
        new_line = line.rstrip()
        my_list.append(new_line)
    print(my_list)
    file.close()

print(read_employees_from_file('outputex2.txt'))