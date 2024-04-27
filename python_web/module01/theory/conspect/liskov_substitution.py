# І з появою нової фігури нам потрібно щоразу вносити зміни в роботу функції total_area. Щоб виправити ситуацію, потрібно
# перекласти обчислення площі фігури на самі класи:
def total_area(shapes):
    sum = 0
    for el in shapes:
        if isinstance(el, Rect):
            sum += el.width * el.height
        if isinstance(el, Circle):
            sum += el.radius ** 2 * pi
    return sum
# Тепер давайте розглянемо, як можна порушити LSP не таким очевидним способом. Припустимо, ми розробляємо програму, як
# працює з геометричними фігурами. У ній є клас для роботи з прямокутниками:
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area_of(self):
        return self.width * self.height
# Тепер потрібно реалізувати фігуру квадрат. Квадрат – це очевидно прямокутник і цілком логічно, що клас Square повинен
# бути спадкоємцем класу Rect
class Square(Rect):
    def __init__(self, size):
        Rect.__init__(self, size, size)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
# І якщо у функції ми використовуємо клас Rect, а працюємо з конкретним класом Square, то можуть виникнути проблеми:
def test_shape_size(shape):
    shape.set_width(10)
    shape.set_height(20)
    return shape.area_of() == 200  # умова не спрацює, якщо shape — екземпляр класу Square
# Відповідно до LSP нам необхідно використовувати спільний інтерфейс для обох класів і не наслідувати Square від Rect.
# Цей спільний інтерфейс повинен бути таким, щоб класи-спадкоємці могли б використовуватися замість батьківських класів,
# від яких вони утворені, не порушуючи роботу програми.
from enum import Enum

class SideType(Enum):
    TYPE_WIDTH = 'width'
    TYPE_HEIGHT = 'height'

class Shape:
    def set_side(self, size, side):
        pass

    def area_of(self):
        pass

class Rect1(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_side(self, size, side):
        if SideType.TYPE_WIDTH == side:
            self.width = size
        if SideType.TYPE_HEIGHT == side:
            self.height = size

    def set_width(self, width):
        self.set_side(width, SideType.TYPE_WIDTH)

    def set_height(self, height):
        self.set_side(height, SideType.TYPE_HEIGHT)

    def area_of(self):
        return self.width * self.height

class Square1(Shape):
    def __init__(self, size):
        self.edge = size

    def set_side(self, size, side=None):
        self.edge = size

    def set_width(self, width):
        self.set_side(width)

    def area_of(self):
        return self.edge ** 2

def get_area_of_shape(figure: Shape):
    return figure.area_of()

if __name__ == '__main__':
    square = Square1(10)
    rect = Rect1(5, 10)
    print('Square area: ', get_area_of_shape(square))
    print('Rect area: ', get_area_of_shape(rect))

# Тепер поведінка спадкоємців не конфліктує із поведінкою базового класу. Це дозволить використовувати і Rect, і Square
# там, де оголошено використання Shape.