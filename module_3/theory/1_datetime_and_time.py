# Модулі datetime та time. Робота з випадковими величинами. Модуль math.
# Робота з датою
#
#
# Python містить інструменти, призначені для роботи з датою і часом, які дозволяють представляти їх у форматі, зрозумілому для користувачів. Ви звикли до стандартного відображення дати в календарях пошти, на веб-сайтах тощо.
#
# Однак у програмуванні дати виглядають інакше, і для здійснення перетворень між різними форматами в Python використовується спеціальний вбудований модуль datetime. Цей модуль надає класи для маніпуляцій з датами і часом.
#
# Основні можливості datetime:
# визначення поточної дати і часу;
# обчислення інтервалу між двома подіями;
# визначення дня тижня, високосного року для будь-якої дати у минулому не раніше року datetime.MINYEAR або в майбутньому не пізніше року datetime.MAXYEAR;
# порівняння дати і часу декількох подій за допомогою операторів порівняння;
# робота з часовими зонами, порівняння подій з урахуванням часових зон та переходу на літній/зимовий час;
# перетворення дати/часу в рядок і навпаки.
#
# Перед роботою з датами і часом потрібно імпортувати модуль в нашому скрипті:
#
# import datetime
#
# Для отримання поточної дати і часу використовується метод datetime.now():
#
# ✂️ Цей код можна запустити!
#
# import datetime
# now = datetime.datetime.now()
# print(now)
#
# Виведення у форматі рік-місяць-день години:хвилини:секунди.мікросекунди:
# 2023-12-14 12:39:29.992996
# Роботу з модулями ми ще розглянемо, але об'єкт datetime в свій скрипт ми також можемо отримати, просто витягнув його з модуля:
#
# from datetime import datetime
#
# Так — і модуль і об'єкт мають однакове ім'я, ви все вірно зрозуміли. 😉
#
# У результаті виклику методу now() ми отримуємо об'єкт datetime, у якого є ряд корисних атрибутів:
#
# from datetime import datetime
#
# current_datetime = datetime.now()
#
# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)
# print(current_datetime.tzinfo)
#
# Ось основні з них:
#
# year: Повертає рік дати. Наприклад, якщо now містить дату "2023-12-14 12:39:29", now.year буде 2023.
# month: Повертає місяць як число від 1 до 12. У нашому прикладі now.month буде 12.
# day: Повертає день місяця. Для "2023-12-14 12:39:29" now.day буде 14.
# hour: Повертає годину дня від 0 до 23. У нашому випадку now.hour буде 12.
# minute: Повертає хвилини часу від 0 до 59. Для даної дати now.minute буде 39.
# second: Повертає секунди часу від 0 до 59. В нашому прикладі now.second буде 29.
# microsecond: Повертає мікросекунди часу. Це значення може бути від 0 до 999999. У "2023-12-14 12:39:29.992996", now.microsecond буде 992996.
# tzinfo: Повертає інформацію про часову зону об'єкта datetime. Для now, якщо часова зона не була вказана, tzinfo буде None.
#
#
# В об'єкта datetime є методи, щоб отримати дату (без часу) та час (без дати):
#
# ✂️ Цей код можна запустити!
#
# from datetime import datetime
#
# current_datetime = datetime.now()
# print(current_datetime.date())
# print(current_datetime.time())
#
# Виведення:
#
# 2023-12-14
# 12:59:06.709007
#
# Є зворотний метод datetime.combine який використовується для створення нового об'єкта datetime шляхом комбінування об'єктів date та time. Це дозволяє створювати точний момент часу, вказуючи дату та час окремо, а потім об'єднуючи їх.
#
# Основний синтаксис:
#
# datetime.datetime.combine(date_object, time_object)
#
# date_object: Об'єкт date, який містить інформацію про рік, місяць та день.
# time_object: Об'єкт time, який містить інформацію про години, хвилини, секунди та мікросекунди.
# Розглянемо приклад:
#
# ✂️ Цей код можна запустити!
#
# import datetime
#
# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)
#
# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)
#
# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"
#
# У цьому прикладі ми створюємо об'єкт date для представлення конкретної дати (14 грудня 2023 року) і об'єкт time для представлення конкретного часу (12:30:15). Потім ми використовуємо datetime.combine для створення нового об'єкта datetime, який представляє цей конкретний момент часу.
#
# Цей метод є корисним, коли у вас є окремі компоненти дати та часу, які потрібно об'єднати для отримання точного моменту в часі.
#
# Щоб створити об'єкт datetime з конкретною вибраною датою у Python, можна використовувати конструктор класу datetime.datetime, передаючи йому рік, місяць, і день як аргументи. Також можна вказати годину, хвилину, секунду та мікросекунду, але це не обов'язково — якщо їх пропустити, вони будуть встановлені на 0.
#
# Для створення об'єкта datetime з певною датою:
#
# ✂️ Цей код можна запустити!
#
# import datetime
#
# # Створення об'єкта datetime з конкретною датою
# specific_date = datetime.datetime(year=2020, month=1, day=7)
#
# print(specific_date)  # Виведе "2020-01-07 00:00:00"
#
# У цьому прикладі створюється об'єкт datetime для 7 січня 2020 року. Оскільки час не вказано, він автоматично встановлюється на початок дня (00:00:00).
#
# Виведення:
#
# 2020-01-07 00:00:00
#
# Створення об'єкта datetime з датою та часом
#
# ✂️ Цей код можна запустити!
#
# import datetime
#
# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)
#
# print(specific_datetime)  # Виведе "2020-01-07 14:30:15"
#
# Виведення:
#
# 2020-01-07 14:30:15
#
# Тут створюється об'єкт datetime для 7 січня 2020 року о 14:30:15.
#
# Використання ключових параметрів допомагає уникнути плутанини та забезпечує чіткість при вказівці конкретних компонентів часу. Наприклад попередній приклад можна було записати так:
#
# ✂️ Цей код можна запустити!
#
# import datetime
#
# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)
#
# print(specific_datetime)  # Виведе "2020-01-07 14:30:15"
#
# Але використання ключових параметрів робить код більш зрозумілим, особливо коли його читають інші розробники. Також це дозволяє легко вказувати тільки ті компоненти дати/часу, які вам потрібні, та уникнути помилок зі змішуванням порядку параметрів.
#
# Метод weekday() використовується для отримання номера дня тижня для вказаної дати. Він повертає номер дня тижня, де понеділок має номер 0, а неділя - 6.
#
# ✂️ Цей код можна запустити!
#
# from datetime import datetime
#
# # Створення об'єкта datetime
# now = datetime.now()
#
# # Отримання номера дня тижня
# day_of_week = now.weekday()
#
# # Поверне число від 0 (понеділок) до 6 (неділя)
# print(f"Сьогодні: {day_of_week}")
#
# У прикладі вище 14 грудня 2023 року було четвер. Виведення:
#
# Сьогодні: 3
#
# Метод часто використовується в сценаріях, де потрібно визначити день тижня для певної дати, наприклад, при створенні календарів, плануванні подій або в обчисленнях, пов'язаних з робочими днями. Він також корисний для встановлення умов в залежності від дня тижня.
#
# Для порівняння двох об'єктів datetime у Python, ви можете використовувати стандартні оператори порівняння, такі як == (рівність), != (нерівність), < (менше), > (більше), <= (менше або дорівнює) та >= (більше або дорівнює). Ці оператори дозволяють порівнювати дати та часи, щоб визначити, чи один об'єкт datetime передує, наступає або є точно таким самим як інший.
#
# ✂️ Цей код можна запустити!
#
# from datetime import datetime
#
# # Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)
#
# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2
#
# Виведення:
# False
# True
# True
# False
# Ключові аспекти: методи роботи з датами і часом
#
# datetime.now(): Метод повертає об'єкт datetime, який містить поточну дату та час.
# datetime.date(): Цей метод повертає об'єкт date, який представляє лише дату (без часу).
# datetime.time(): Метод повертає об'єкт time, який містить лише час (без дати).
# datetime.combine(date, time): Цей метод використовується для об'єднання об'єктів date та time і створення нового об'єкта datetime.
# datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0): Конструктор класу datetime дозволяє створити об'єкт datetime з конкретною датою та часом.
# weekday(): Метод визначає номер дня тижня для вказаної дати, де понеділок має номер 0, а неділя - 6.
#
# Методи порівняння об'єктів datetime:
#
# == (рівність): Порівнює, чи є дві дати рівні.
# != (нерівність): Порівнює, чи дві дати не є рівними.
# < (менше): Визначає, чи одна дата передує іншій.
# > (більше): Визначає, чи одна дата наступає за іншою.
# <= (менше або дорівнює): Порівнює, чи одна дата менше або дорівнює іншій.
# >= (більше або дорівнює): Порівнює, чи одна дата більше або дорівнює іншій.
# Робота з часовими проміжками timedelta
#
# У модулі datetime є клас timedelta, який використовується для представлення різниці між двома моментами в часі. Об'єкти timedelta можуть представляти дні, години, хвилини, секунди та мікросекунди. Вони корисні для розрахунків, що включають додавання або віднімання часу від конкретних дат або порівняння часових інтервалів.


from datetime import datetime, timedelta

# Створення об'єкта datetime
now = datetime.now()

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

# Об'єкт timedelta можна створити, задаючи тижні, дні, години, хвилини, секунди, мілісекунди і мікросекунди, передавши
# один або кілька з таких параметрів: days, seconds, microseconds, milliseconds, minutes, hours, weeks. Якщо якийсь
# параметр не заданий, то він дорівнює 0 за замовчуванням.

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

# Якщо відняти від одного datetime об'єкту інший, то отримаємо timedelta об'єкт. Він відповідає за відрізок часу між
# двома датами.
seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)
print(difference.total_seconds())

now = datetime.now()
future_date = now + timedelta(days=10, hours=1)
print(future_date)

four_weeks_interval = timedelta(days=28)
print(seventh_day_2020 - four_weeks_interval)
print(seventh_day_2020 + four_weeks_interval)

# Але якщо потрібно робити обчислення або порівняння, засновані на послідовності дат, наприклад, для визначення
# кількості днів між двома датами.
#
# Ми можемо використати метод toordinal(), який повертає порядковий номер дня, враховуючи кількість днів з 1 січня року
# 1 нашої ери (тобто з початку християнського календаря). Цей метод перетворює об'єкт datetime в ціле число, що
# представляє порядковий номер даного дня.
# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")

# Наприклад ми хочемо визначити скільки пройшло повних днів, коли Наполеон спалив Москву, а це відбулося 14 вересня 1812 року
# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)

# Отже пройшов 77,161 день від цієї дати станом на поточну дату (18.12.2023) запуску коду. Якщо ви запустите цей код
# самостійно число днів звісно збільшиться. Спробуйте 😉


# Робота з timestamp
# У контексті програмування та обробки даних, термін timestamp (часова мітка) використовується для вказівки конкретного
# моменту в часі. Це зазвичай представляється як кількість секунд (або мілісекунд/мікросекунд у деяких системах) з
# певної початкової дати, найчастіше з 1 січня 1970 року в UTC, це часовий пояс Гринвіча. Детально про сам UTC поговоримо
# трошки далі. Поки timestamp для нас це просто прийнята константа і нічого особливого вона не означає. Просто для
# зручності люди колись почали відраховувати час в секундах з цієї миті і це виявилося дуже зручно. Є стандартним
# способом представлення часу в багатьох операційних системах та програмних мовах.
#
# Адже порівняти два числа завжди легше і швидше, ніж порівняти складну структуру дат і часів. Ви зустрінете використання
# timestamp в програмуванні, базах даних, логуванні подій та при збереженні інформації про часові моменти подій.
#
# ☝ timestamp є універсальним способом представлення часу, оскільки він не залежить від часових зон і календарних систем.
# У Python ви можете перетворити об'єкт datetime в timestamp і навпаки. Конвертація datetime в timestamp
#
# ✂️ Цей код можна запустити!

# Поточний час
now = datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу

# Виведення:
# 1709902524.41355

# Конвертація timestamp в об'єкт datetime
# ✂️ Цей код можна запустити!
# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime
# Виведення:
# 2021-03-31 12:40:00

