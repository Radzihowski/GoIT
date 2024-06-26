# Іменовані кортежі
import collections
# Використання кортежів у Python для передачі даних між функціями обробниками — це хороша та поширена практика. Але є
# одна незручність у кортежів - нам необхідно пам'ятати індексацію елементів у кортежі і не плутати їх порядок. Це не
# завжди зручно і для ситуацій, коли в кортежі є досить багато елементів, такий підхід ускладнює читабельність коду.
#
# Тому були придумані іменовані кортежі namedtuple в Python. Це розширення стандартного типу даних tuple, яке дозволяє
# виконувати доступ до елементів списку за іменем, а не за індексом. Що робить наш код легшим для читання та більш зрозумілим.
# Іменований кортеж створюється за допомогою функції namedtuple з модуля collections.
from collections import namedtuple
# Створення іменованого кортежу
Point = namedtuple('Point', ['x', 'y'])

# У цьому прикладі Point іменований кортеж, який має поля-імена x та y. Тепер ми можемо звертатися до елементу такого
# кортежу за іменем:
# Створення екземпляра Point
p = Point(11, y=22)

# Доступ до елементів
print(p.x)  # 11
print(p.y)  # 22

# Створення іменованого кортежу Person
Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', "birth_place", "post_index"])

# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# Виведення різних атрибутів іменованого кортежу
print(person.first_name)
print(person.post_index)
print(person.age)
print(person[3])

# Виведення:
# Mick
# 01146
# 35
# Boston

# Тепер, використовуючи іменований кортеж Person, ви можете створювати кортежі, які обов'язково повинні містити 5 елементів
# і у таких кортежів, окрім індексів, є імена. Кожен елемент кортежу може бути отриманий як за іменем, так і за індексом,
# що забезпечує гнучкість у доступі до даних. За такого підходу вам достатньо один раз визначити Person і більше не
# повертатися до нього, щоб згадати, який елемент за що відповідає.
#
# Розглянемо, ще один приклад використання іменованого кортежу при представленні інформації про кота. Цей код є чудовим
# прикладом використання іменованих кортежів для зручного та зрозумілого управління даними.

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Simon', 4, 'Krabat')

print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')

# Виведення:
# This is Simon, a 4-year-old cat. His owner is Krabat.
# Ми використали namedtuple для створення іменованого кортежу Cat з полями nickname, age, owner. Далі ми створюємо
# змінну cat з ім'ям 'Simon', віком 4 роки і власником 'Krabat'. Виводимо інформацію про кота в форматованому рядку,
# використовуючи поля іменованого кортежу Cat. Це робить код більш організованим і легким для розуміння.
#
# Бо наприклад наступний рядок коду набагато менш інформативний в нашому випадку.
print(f'This is a cat {cat[0]}, {cat[1]} age, his owner {cat[2]}')
# Іменовані кортежі в Python - це потужний інструмент для створення структур даних, які є незмінними та більш зрозумілими,
# ніж звичайні кортежі. Вони особливо корисні для програм, які маніпулюють складними наборами даних і потребують чіткої структури.

