# Повернемося до завдання розрахунку коренів квадратного рівняння з попереднього модуля.
#
# Необхідно обчислити коріння квадратного рівняння.
#
# a · x2 + b · x + c = 0
#
# Дискримінант рівняння помістіть у змінну D
#
# D = b2 - 4 · a · c
#
# Коріння рівняння помістіть у змінні x1 та x2
#
# x1 = (-b + D0.5) / (2 · a)
#
# x2 = (-b - D0.5) / (2 · a)
#
# Минулого разу ми просто вказали значення коефіцієнтів a, b, c. Тепер, коли ми вже знаємо про розгалуження, ми можемо
# перевіряти значення дискримінанта і, в залежності від того додатне чи від'ємне, провести розрахунок коренів.
# Виконайтерозрахунок коренів для довільних значень коефіцієнтів a, b, c.

import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
