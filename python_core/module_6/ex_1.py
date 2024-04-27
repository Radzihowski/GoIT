# Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.
# Приклад файлу:
# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
# Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.
# Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл і
# повертати загальну суму заробітної плати всіх розробників компанії.

# Вимоги до завдання:
# функція total_salary повертає значення типу float
# для читання файлу функція total_salary використовує лише метод readline
# ми поки що не використовуємо менеджер контексту with

# This variant goes to the solution
def total_salary(path):
    file = open(path, 'r')

    result = 0.0

    while True:
        line = file.readline()
        if not line:
            break
        split_line = line.strip().split(",")
        result = result + float(split_line[1])
    file.close()
    return result

# А на цьому варіанті я тренувався:
def total_salary(path):
    file = open('text1.txt', 'r')

    result = 0.0

    while True:
        line = file.readline()
        if not line:
            break
        split_line = line.strip().split(",")
        print(result)
        print(split_line[0])
        print(split_line[1])
        result = result + float(split_line[1])
    file.close()
    return result

print(total_salary('text1.txt'))

