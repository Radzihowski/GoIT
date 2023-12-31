# Напишіть функцію визначення кількості днів у конкретному місяці. Ваша функція повинна приймати два параметри:
# month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 і year - рік, що складається із чотирьох цифр.
# Перевірте, чи функція коректно обробляє місяць лютий високосного року.

from datetime import date
from calendar import monthrange


def get_days_in_month(month, year):
    days = monthrange(year, month)
    print(days[1])
    return days[1]

get_days_in_month(5, 2016)
