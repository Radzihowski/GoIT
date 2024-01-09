# Реалізувати функцію, яка повертає n числа, що зустрічаються найчастіше і n чисел, що найменш часто зустрічаються,
# з файлу
#
# Посилання на файл numbers.txt

from collections import Counter

def num_counter(filename, n):
    with open(filename, 'r') as file:
        data = file.read()
    counter = Counter(int(i) for i in data.split(','))
    order = counter.most_common(len(counter))
    return [i for i in order[:n]], [i for i in order[-n:]]

most, least = num_counter('numbers.txt', 10)
print(f"Most {most} \n Least {least}")