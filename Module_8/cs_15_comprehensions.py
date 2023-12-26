# Comprehensions
# comprehensions - це синтаксична конструкція Python, створена спеціально, щоб зменшити кількість коду, коли потрібно
# для кожної ітерації циклу for додати один елемент у нову колекцію.


squares = list()

for i in range(10):
    squares.append(i ** 2)

print(squares)

squares_comp = [i**2 for i in range(10)]
print(squares_comp)

print(squares == squares_comp)

from math import sqrt, pow, pi
squares_comp = [round(sqrt(pow(pi, i)), 2) for i in range(10)]
print(squares_comp)