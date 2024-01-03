# Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі ISO '2021-05-27 17:08:34.149Z' у
# вигляді наступного рядка 'Thursday 27 May 2021' - день тижня, число, місяць та рік. Перетворене значення функція
# повертає під час виклику.

from datetime import datetime


def get_str_date(date):
    # Перетворюємо вхідну дату з рядка у об'єкт datetime
    date_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    print(date_object)
    # форматуємо дату у бажаний вигляд
    formated_date = date_object.strftime('%A %d %B %Y')
    print(formated_date)
    return  formated_date


print(get_str_date('2021-05-27 17:08:34.149Z'))

# для вирішення ми скористались двума головними методами strptime and strftime are both functions used for formatting
# and parsing dates and times in Python, but they serve different purposes