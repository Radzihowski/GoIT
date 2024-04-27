# Реалізуйте функцію get_discount_price_customer для розрахунку ціни на товар інтернет-магазину з урахуванням знижки клієнта.
#
# Функція приймає два параметри:
#
# price — ціна продукту
# customer — словник з даними клієнта такого виду: {"name": "Dima"} або {"name": "Boris", "discount": 0.15}
# Ви маєте глобальну змінну DEFAULT_DISCOUNT, яка визначає знижку для клієнта, якщо у нього немає поля discount.
#
# Функція get_discount_price_customer має повертати нову ціну товару для клієнта.
#
# Нагадаємо, що дисконт discount - це дробове число від 0 до 1. І ми під знижкою розуміємо коефіцієнт, який визначає
# величину ціни. І на цю величину ми знижуємо підсумкову ціну товару: price = price * (1 - discount).

DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if 'discount' in customer.keys():
        # print(customer['discount']) /only for troubleshooting reason
        discount = customer['discount']
    else:
        # print('Key doesn\'t exist') /only for troubleshooting reason
        discount = DEFAULT_DISCOUNT
    return price * (1 - discount)


print(get_discount_price_customer(10, {'name': 'Dima'}))
print(get_discount_price_customer(10, {'name': 'Boris', 'discount': 0.15}))
