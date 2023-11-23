# Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні. Реалізуйте функцію lookup_key для
# всіх ключів за значенням у словнику. Першим параметром у функцію ми передаємо словник, а другим — значення, що хочемо
# знайти. Таким чином, результат може бути як список ключів, так і порожній список, якщо ми нічого не знайдемо.

def lookup_key(data, value):
    result = []
    for k, v in data.items():
        if v == value:
            result.append(k)
    return result

print(lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))

