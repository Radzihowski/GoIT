# У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:
#
# ['Robert Stivenson,28', 'Alex Denver,30']
# Це список рядків із прізвищем та віком співробітника, розділеними комами.
#
# Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника починалася з
# нового рядка.
#
# Функція запису в файл write_employees_to_file(employee_list, path), де:
#
# path – шлях до файлу.
# employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
# [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# Вимоги:
#
# запишіть вміст employee_list у файл, використовуючи режим "w".
# ми поки що не використовуємо менеджер контексту with
# кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:
# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19

def write_employees_to_file(employee_list, path):
    file = open(path, 'w')
    string_new = ''
    for el in employee_list:
        string = '\n'.join(el)
        print(string)
        string_new = string + '\n'
    file.close()

# Тестовий варіант на якому я тренувався
def write_employees_to_file():
    file = open('outputex2.txt', 'w')
    employee_list = [['Robert Stivenson,28'], ['Alex Denver,30'], ['Drake Mikelsson,19']]
    string_new = ''
    for el in employee_list:
        string = '\n'.join(el)
        print(string)
        string_new += string + '\n'
    file.write(string_new)
    file.close()

print(write_employees_to_file())
