# Для функції попереднього завдання створіть рядки документації. Можна використовувати наступний шаблон
# """Функція повертає суму за доставлення замовлення.
#
#  Перший параметр &mdash; кількість товарів в замовленні.
#  Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""

def cost_delivery(quantity, *_, discount=0):
    """ Function return price for the order
    First parameter number of orders where first order cost 5 and all the rest 2
    :parameter discount if 0 or absent - no discount
    """

    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result
