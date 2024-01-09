# Напишіть функцію, що приймає на вхід три цілих числа: день, місяць і рік. Функція повинна повертати порядковий номер
# заданого дня в зазначеному році і також день тижня.
#
# Порядкова дата містить номер року і порядковий номер дня в цьому році - обидва в цілочисельному форматі. При цьому
# рік може бути будь-яким згідно з григоріанським календарем, а номер дня - числом в інтервалі від 1 до 366

from datetime import datetime, date

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def day_of_year(full_date):
    year, month, day = [int(i) for i in full_date.split('-')]
    day_of_week = datetime(year=year, month=month, day=day).weekday()
    print(day_of_week)
    day_zero = date(year, 1, 1).toordinal() - 1
    print(day_zero)
    current_day = date(year, month, day).toordinal()
    print(current_day)
    day_from_year_start = current_day - day_zero
    return days_name.get(day_of_week), year, day_from_year_start

print(day_of_year('2021-02-21'))