# Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі ISO '2021-05-27 17:08:34.149Z' у
# вигляді наступного рядка 'Thursday 27 May 2021' - день тижня, число, місяць та рік. Перетворене значення функція
# повертає під час виклику.

from datetime import datetime


def get_str_date(date):
    s = datetime.fromisoformat(date[:-1])
    print(s)
    return


print(get_str_date('2021-05-27 17:08:34.149Z'))