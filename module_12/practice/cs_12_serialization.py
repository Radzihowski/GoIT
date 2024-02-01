# Керування порядком серіалізації
# Реалізувати pickable клас, який зберігає дату і час коли об'єкт цього класу серіалізували і коли розпакувал

import pickle
from datetime import datetime
from time import sleep


class RememberAll:
    def __init__(self, *args):
        self.data = list(args)
        self.saved = None
        self.restored = None

    def __getstate__(self):
        # Копіюємо стан об'єкта із self.__dict__, який містить
        # усі атрибути нашого екземпляра. Завжди використовуйте dict.copy()
        # метод, що дає змогу уникнути зміни вихідного стану.
        state = self.__dict__.copy()
        state['saved'] = datetime.now()
        return state

    def __setstate__(self, state):
        # Відновлення атрибутів класу(наприклад, ім'я файлу і номер строки)
        self.__dict__.update(state)
        self.restored = datetime.now()


list_data = RememberAll(1, 2, 3)
print(list_data.data)

test_saving = pickle.dumps(list_data)
sleep(3)
loaded_data = pickle.loads(test_saving)
print(loaded_data.saved)
print(loaded_data.restored)

