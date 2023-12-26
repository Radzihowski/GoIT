# deque
# collections.deque(iterable, [maxlen]) - створює чергу з ітерованого об'єкта з максимальною довжиною maxlen.
# Черги дуже схожі на списки, за винятком того, що додавати і видаляти елементи можна або справа, або зліва.
#
# Методи, визначені в deque:
# append(x) - додає x у кінець.
# appendleft(x) - додає x на початок.
# clear() - очищає чергу.
# count(x) - кількість елементів, що дорівнюють x.
# extend(iterable) - додає в кінець усі елементи iterable.
# extendleft(iterable) - додає в початок усі елементи iterable (починаючи з останнього елемента iterable).
# pop() - видаляє і повертає останній елемент черги.
# popleft() - видаляє і повертає перший елемент черги.
# remove(value) - видаляє перше входження value.
# reverse() - розгортає чергу.
# rotate(n) - послідовно переносить n елементів з початку в кінець (якщо n від'ємне, то з кінця в початок).

from collections import deque
def_list = list(range(2, 7))
print(def_list)

my_q = deque(def_list)
print(my_q)
print(deque(def_list, 3))

my_q = deque(def_list, 10)
print(my_q)

for i in range(10):
    my_q.appendleft(i)
    print(my_q)

