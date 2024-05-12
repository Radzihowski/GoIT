# Тип Any
#
# Це спеціальний тип, який інформує статичну перевірку типів таким чином, що кожен тип сумісний з цим ключовим словом.
#
# Розглянемо нашу стару функцію calculator, що тепер приймає аргументи будь-якого типу.

from typing import TypeVar, Any

T = TypeVar("T", int, str, float)

def calculator(x: Any, y: Any) -> T:
    return x + y

print(calculator(3, 5))
print(calculator("Hello", " World"))
print(calculator(3.5, 1.4))

# Це не дуже "хороший" тип і використовувати його потрібно завжди усвідомлено