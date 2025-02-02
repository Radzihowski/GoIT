"""Додаємо дані

Далі напишемо скрипт seeds.py, щоб наповнити даними нашу БД. Підключаємо всі моделі та імпортуємо модуль connect.py,
для підключення до нашої хмарної БД MongoDB. Інші коментарі є в коді файлу seeds.py"""

from models import Notes, Record, Tag
import connect

# спочатку - створити об'єкт Tag
tag = Tag(name='Purchases')
# потім - створення об'єктів Record
record1 = Record(description='Buying sausage')
record2 = Record(description='Buying milk')
record3 = Record(description='Buying oil')
#  Останнє - створюємо об'єкт Note і зберігаємо його
Notes(name='Shopping', records=[record1, record2, record3], tags=[tag, ]).save()

Notes(name='Going to the movies', records=[Record(description='Went to see the Avengers'), ], tags=[Tag(name='Fun'), ]).save()

