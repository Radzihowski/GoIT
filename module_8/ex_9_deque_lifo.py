# За допомогою колекції deque реалізуйте структуру даних LIFO. Створіть змінну lifo, що містить 
# колекцію deque. Обмежте розмір за допомогою константи MAX_LEN. Функція push додає значення element 
# на початок списку lifo. Функція pop дістає та повертає перше значення зі списку lifo.
from collections import deque

MAX_LEN = 3

lifo = deque(maxlen=MAX_LEN)


def push(element):
    print(len(lifo))
    # if len(lifo) > MAX_LEN :
    #     lifo.pop()
    #     lifo.appendleft(element)
    #     print("IF statement")
    # else:
    #     print(lifo)
    #     lifo.appendleft(element)
    print(lifo)
    lifo.appendleft(element)
    print(lifo)

def pop():
    return lifo[0]

push('first')
push('second')
push('third')
push('forth')
push('fifth')
push('sixth')
push('seventh')
print(pop())