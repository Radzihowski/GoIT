"""
Метод: split
​
Напишемо універсальну функцію get_parameters, яка повертатиме словник з даними.
Оскільки в першому рядку розділювачем є символ `;` а в другому `&`,
тому тут вдало підійде випадок (a|b - відповідає a або b)
"""

import re

url_query = "20850=ot-25-mp-do-47-mp;23777=6-6-5;38435=8-gb;41404=16gb"  # ;
url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"  # &
url = "data=value*data_1=value_1"
ur2 = "dadddddddta=vaddddddlue%daddddta_1=valdddddue_1"
def get_parameters(data: list) -> dict:
    obj_query = {}
    for element in data:
        key, value = element.split('=')
        obj_query.update({key: value.replace('+', ' ')})
    return obj_query
data = re.split(r';|&', url_query)
print(data)
data = re.split(r';|&|\*|%', url_search)
print(data)
data = re.split(r';|&|\*|%', url)
print(data)
data = re.split(r';|&|\*|%', ur2)
print(data)
# ['20850=ot-25-mp-do-47-mp', '23777=6-6-5', '38435=8-gb', '41404=16gb']
# ['q=Cat+and+dog', 'ie=utf-8', 'oe=utf-8', 'aq=t']
# ['data=value', 'data_1=value_1']