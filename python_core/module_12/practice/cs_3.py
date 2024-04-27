# Серіалізація об'єктів Python за допомогою pickle
from pickle import dumps, loads


class Absolute:
    x_variable = 'some'

    def __init__(self):
        print('New A!')
        self.y_variable = 'another'

class_a = Absolute()

serialization_class_a = dumps(class_a)
serialization_Absolute = dumps(Absolute)

restored_class_a = loads(serialization_class_a)
restored_Absolute = loads(serialization_Absolute)

print(class_a.x_variable, class_a.y_variable)
print(restored_class_a.x_variable, restored_class_a.y_variable)
print(dir(restored_Absolute))