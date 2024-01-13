# LIFO (англ. last in, first out, "останнім прийшов - першим пішов") - спосіб організації даних або іншими словами Стек
# (Stack). У структурованому лінійному списку, організованому за принципом LIFO, елементи можна додавати та обирати
# тільки з одного кінця, який називається "вершиною списку".

from collections import deque

MAX_LEN = 10

lifo = deque(maxlen=MAX_LEN)

def push(element):
    lifo.appendleft(element)

def pop():
    lifo.popleft()

push('Biba')
push('Boba')
print(lifo)
pop()
push('Carl')
print(lifo)