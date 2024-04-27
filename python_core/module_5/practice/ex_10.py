# Напишіть функцію find_word, яка приймає два параметри: перший text та другий word. Функція виконує пошук зазначеного
# слова word у тексті text за допомогою функції search та повертає словник.
#
# При виклику функції:

# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and "
#     "first released it in 1991 as Python 0.9.0.",
#     "Python"))
# Результат має бути наступного виду при збігу:

# {
#     'result': True,
#     'first_index': 34,
#     'last_index': 40,
#     'search_string': 'Python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming'
#               'language, and first released it in 1991 as Python 0.9.0.'
# }
# де
#
# result — результат пошуку True або False
# first_index — початкова позиція збігу
# last_index — кінцева позиція збігу
# search_string — частина рядка, в якому був збіг
# string — рядок, переданий у функцію
# Якщо збігів не виявлено:

# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and"
#     "first released it in 1991 as Python 0.9.0.",
#     "python"))
# Результат:

# {
#     'result': False,
#     'first_index': None,
#     'last_index': None,
#     'search_string': 'python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# }

import re

dictionary = {}


def find_word(text, word):
    for _ in word:
        if word in text:
            result = True
            search_word = re.search(word, text)
            pos = search_word.span()
            dictionary.update({"result": result, "first_index": pos[0], "last_index": pos[1], "search_string": word,
                               "string": text})
        else:
            result = False
            dictionary.update(
                {"result": result, "first_index": None, "last_index": None, "search_string": word, "string": text})

    return dictionary


print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.","Python"))
