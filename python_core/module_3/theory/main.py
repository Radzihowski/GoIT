from datetime import datetime
import datetime

# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2020, month=1, day=7, hour=12)

print(specific_date)  # Виведе "2020-01-07 00:00:00"

# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:

