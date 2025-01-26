"""
Є словник data в який треба додати значення в список під ключем 'names'
якщо ключ існує то додати значення в існуючий список
якщо ключа не існує - то створити пустий список з елементом
Приклад:
data = {}

def add_value(val: str):
    pass

print(add_value("Vlad")) # повинно повернути {"names": ["Vlad"]}
print(add_value("Nick")) # повинно повернути {"names": ["Vlad", "Nick"]}

"""

data = {}

def add_value(val: str):
    ...

print(add_value("Vlad")) # повинно повернути {"names": ["Vlad"]}
print(add_value("Nick")) # повинно повернути {"names": ["Vlad", "Nick"]}