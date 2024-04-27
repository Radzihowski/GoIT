# Цей принцип допомагає вирішувати проблему, коли невелика зміна в одній частині системи викликає лавину змін в інших частинах. Якщо у програмі при зміні поліпшення потрібно виправити десятки модулів, така система, швидше за все, спроектована погано.
#
# Принцип відкритості-закритості декларує, що модулі повинні бути відкриті для розширення, але закриті для зміни.
#
# Іншими словами — модулі потрібно проектувати так, щоб їх не можна було змінювати, а нова функціональність у програмі повинна з'являтися лише за допомогою створення нових сутностей та композиції їх зі старими. Звичайно, завжди є зміни, які неможливо внести, не змінивши код якогось модуля — жодна система не може бути закрита від змін повністю.
#
# Щоб зрозуміти принцип, потрібно розглянути застосування його у місцях з'єднання модулів.
#
# Розглянемо наступний приклад:
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def total_area(shapes):
    sum = 0
    for el in shapes:
        sum += el.width * el.height
    return sum


if __name__ == '__main__':
    shapes = [Rect(10, 10), Rect(4, 5), Rect(3, 3)]
    area = total_area(shapes)
    print(area)

# Є клас Rect, що описує прямокутник, і є функція total_area, яка обчислює загальну площу фігур. У чому може виникнути
# неприємність для такого коду?
#
# Якщо у нас з'явиться нова фігура, наприклад, коло — Circle, нам доведеться змінити роботу функції total_area.

from math import pi


class Rect1:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


def total_area(shapes):
    sum = 0
    for el in shapes:
        if isinstance(el, Rect):
            sum += el.width * el.height
        if isinstance(el, Circle):
            sum += el.radius ** 2 * pi
    return sum


if __name__ == '__main__':
    shapes = [Rect1(10, 10), Circle(5), Rect1(4, 5), Rect1(3, 3), Circle(3)]
    area = total_area(shapes)
    print(area)

# І з появою нової фігури нам потрібно щоразу вносити зміни в роботу функції total_area. Щоб виправити ситуацію, потрібно
# перекласти обчислення площі фігури на самі класи:

class Rect2:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height

class Circle2:
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return self.radius ** 2 * pi

def total_area(shapes):
    sum = 0
    for el in shapes:
        sum += el.area_of()
    return sum

if __name__ == '__main__':
    shapes = [Rect2(10, 10), Circle2(5), Rect2(4, 5), Rect2(3, 3), Circle2(3)]
    area = total_area(shapes)
    print(area)
