# Паттерн проектування, який гарантує, що клас має лише один екземпляр і надає до нього глобальну точку доступу.
#
# Одинак вирішує дві проблеми:
# - Гарантує наявність єдиного екземпляра класу.
# - Надає глобальну точку доступу.

import random

class Singletone:
    """Classic singleton"""
    __instance = None

    def __init__(self):
        self.number = random.randint(1, 10)

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(Singletone)
        return cls.__instance

class Regular:
    """Simple class to compare behaviour"""
    def __init__(self, *args, **kwargs):
        self.number = random.randint(1, 10)

def testing():
    print("Singleton instances")
    list_singleton = [Singletone() for i in range(0, 5)]
    for index, element in enumerate(list_singleton):
        print(f"Element: {index}, number: {element.number}")

    print("Instances of a regular class")
    list_regular = [Regular() for i in range(0, 5)]
    for index, element in enumerate(list_regular):
        print(f'Element: {index}, number: {element.number}')

if __name__ == "__main__":
    testing()

# Паттерн одинак гарантує, що жодний інший код не замінить створений екземпляр класу, тому ви завжди впевнені в наявності
# лише одного об'єкта-одинака. І як бачимо з прикладу, одинак завжди повертає 10, в той час як звичайний клас у нас
# виводитьрізні довільні числа.