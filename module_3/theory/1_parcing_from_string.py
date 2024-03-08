from datetime import datetime, timezone
# ПАРСІНГ ДАТИ З РЯДКА
#
# Коли потрібно відобразити дату та час у зрозумілому для людини форматі, ми використовуємо метод strftime. Він застосовується при записувані часових міток у файли логування, при відображані дати та часу на веб-сторінках або в інтерфейсах користувача, а також при форматуванні дат для збереження в базах даних.
#
# Отже метод strftime використовується для форматування об'єктів дати та часу datetime у рядки за допомогою специфічних форматних кодів. Цей метод дає можливість представити дату та час у зручному для читання форматі або в форматі, що відповідає специфічним вимогам.
#
# Синтаксис методу strftime виглядає наступним чином:
# datetime_object.strftime(format)

# Де datetime_object - це об'єкт datetime, а format - рядок формату, який визначає, як дата та час повинні бути представлені.
#
# Кожен код у рядку формату починається з символу % і представляє певний компонент дати або часу. Ось деякі з найбільш використовуваних кодів:
#
# %Y - рік з чотирма цифрами (наприклад, 2023).
# %y - рік з двома цифрами (наприклад, 23).
# %m - місяць як номер (наприклад, 03 для березня).
# %d - день місяця як номер (наприклад, 14).
# %H - година (24-годинний формат) (наприклад, 15).
# %I - година (12-годинний формат) (наприклад, 03).
# %M - хвилини (наприклад, 05).
# %S - секунди (наприклад, 09).
# %A - повна назва дня тижня (наприклад, Tuesday).
# %a - скорочена назва дня тижня (наприклад, Tue).
# %B - повна назва місяця (наприклад, March).
# %b або %h - скорочена назва місяця (наприклад, Mar).
# %p - AM або PM для 12-годинного формату.
#
# Розглянемо декілька прикладів

now = datetime.now()
# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)

# Виведення:
# 2023-12-18 01:37:07
# Monday, 18 December 2023
# 01:37 AM
# 18.12.2023

# Метод strptime в Python використовується для перетворення рядків у об'єкти datetime. Цей метод є протилежністю до
# strftime, який перетворює об'єкти datetime у рядки. strptime дозволяє аналізувати рядки, що містять дату та/або час,
# і перетворювати їх на структуровані об'єкти datetime за допомогою визначеного формату.
#
# Синтаксис методу strptime виглядає наступним чином:
#
# datetime_object = datetime.strptime(string, format)
# де:
# string - рядок, який містить дату та/або час.
# format - рядок формату, який вказує, як розібрати string.
# Коди форматування для strptime такі ж, як і для strftime. Наприклад, %Y представляє рік із чотирма цифрами, %m - місяць
# у вигляді двоцифрового числа тощо.
# Розглянемо випадок коли з веб-сайту є рядок дата "2023.03.14" якогось посту і нам треба перед тим як зберегти дату в
# базі даних перетворити її на об'єкт datetime
# ✂️ Цей код можна запустити!

# Припустимо, у нас є дата у вигляді рядка
date_string = "2023.03.14"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу

# У цьому прикладі рядок date_string перетворюється в об'єкт datetime за допомогою визначеного формату: "2023.03.14" це "%Y.%m.%d".
# Виведення:
# 2023-03-14 00:00:00
# З точки зору застосування, метод strptime корисний, коли потрібно обробляти дати та часи, які отримані у форматі рядка,
# наприклад, з текстових файлів, користувацького вводу, веб-запитів або баз даних. Він дозволяє перетворити ці рядки на
# об'єкти datetime, якими вже потім легко маніпулювати в коді.

# РОБОТА З ISO ФОРМАТОМ ДАТИ
#
# ISO формат дати відноситься до міжнародного стандарту представлення дат і часу, відомого як ISO 8601. Цей стандарт
# створений Міжнародною організацією стандартизації (ISO) та використовується для уніфікації представлення дати та часу
# у всьому світі.
#
# Формат дати в ISO 8601 виглядає як "YYYY-MM-DD", де:

# YYYY - це рік (наприклад, 2023),
# MM - місяць (наприклад, 01 для січня),
# DD - день (наприклад, 31).
#
# Формат часу в ISO 8601 виглядає як "HH:MM:SS", де:

# HH - години (від 00 до 23),
# MM - хвилини (від 00 до 59),
# SS - секунди (від 00 до 59, іноді з додатковими десятковими частинами для мікросекунд).
#
# Повне представлення дати та часу в ISO 8601 поєднує ці два формати з "T" між ними, наприклад "YYYY-MM-DDTHH:MM:SS".
# Це відділяє дату від часу і формат легко відрізняється від інших представлень.
#
# ISO 8601 також підтримує представлення часових зон. Наприклад, "Z" на кінці означає UTC (координований всесвітній час),
# а відхилення від UTC може бути представлене як "+HH:MM" або "-HH:MM". Термін UTC, що розшифровується як Всесвітній
# координований час (англ. Coordinated Universal Time), є основною системою часу, від якої регулюються всі часові зони
# у світі. Він використовується як світовий стандарт часу. Він не змінюється з порами року та не підлягає переходу на
# літній/зимовий час, на відміну від багатьох місцевих часових зон.
#
# Через свою універсальність, UTC широко використовується в міжнародних комунікаціях, авіації, астрономії та інших галузях.
# Локальні часові зони часто визначаються як UTC плюс або мінус певна кількість годин.
#
# Модуль datetime надає зручні інструменти для роботи з датами та часом у форматі ISO 8601. Об'єкт datetime можна легко
# перетворити в рядок формату ISO 8601 за допомогою методу isoformat():

# Поточна дата та час
now = datetime.now()

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)

# Bиведе, наприклад:
#
# 2023-12-14T15:43:42.651309
#
# Для зворотного перетворення рядка у форматі ISO 8601 на об'єкт datetime, можна використати метод fromisoformat():

iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)

# Виведе об'єкт datetime, що відповідає вказаній даті та часу
#
# 2023-03-14 12:39:29.992996

# Метод isoweekday() у об'єкті datetime використовується для отримання дня тижня відповідно до ISO 8601. Згідно з цим
# стандартом, тиждень починається з понеділка, який має значення 1, і закінчується неділею, яка має значення 7.

# Створення об'єкта datetime
now = datetime.now()

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня
# У цьому прикладі day_of_week буде містити число від 1 до 7, де 1 відповідає понеділку, а 7 - неділі.
# Для четверга виведення буде:

# Метод isoweekday() корисний у сценаріях, де потрібно визначити конкретний день тижня, наприклад, при плануванні подій
# або виконанні дій, залежних від дня тижня. Це може бути особливо корисним у бізнес-логіці, яка оперує робочими та
# вихідними днями.
#
# Також розглянемо корисний метод isocalendar(), який використовується для отримання кортежу, що містить ISO рік, номер
# тижня в році та номер дня тижня відповідно до ISO 8601.
#
# Вивід isocalendar() - це кортеж (ISO_рік, ISO_тиждень, ISO_день_тижня), де:
#
# ISO_рік - це рік у форматі ISO.
# ISO_тиждень - номер тижня в році за ISO 8601 (від 1 до 53).
# ISO_день_тижня - день тижня за ISO 8601, де 1 означає понеділок, а 7 - неділю.

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
print(now.isocalendar())
#
# У цьому прикладі iso_calendar буде містити три значення: ISO рік, номер тижня та номер дня тижня, у форматі
# datetime.IsoCalendarDate(year=2023, week=50, weekday=4). Виведення до 14.12.2023 буде:
#
# ISO рік: 2023, ISO тиждень: 50, ISO день тижня: 4
#
# Метод isocalendar() корисний у ситуаціях, коли потрібно працювати з тижневими інтервалами або розраховувати дати у
# форматі, який широко використовується в бізнес-плануванні та логістиці. Він також може бути корисним для визначення
# конкретного тижня року для подій або при плануванні завдань.

# КЛЮЧОВІ АСПЕКТИ: МЕТОДИ ДЛЯ РОБОТИ З ISO ФОРМАТОМ ДАТИ
# Отже, коротко підсумуємо використання методів, які ми щойно розглянули:
# Метод isoformat() використовується для конвертації об'єкта datetime в рядок у форматі ISO 8601.
# Метод fromisoformat() використовується для конвертації рядка у форматі ISO 8601 в об'єкт datetime.
# Метод isoweekday() використовується для отримання дня тижня відповідно до ISO 8601.
# Метод isocalendar() використовується для отримання кортежу, що містить ISO рік, номер тижня в році та номер дня тижня відповідно до ISO 8601.

# РОБОТА З ЧАСОВИМИ ЗОНАМИ
# Щоб вивести дату у форматі UTC це можна зробити, додавши інформацію про часову зону до об'єкта datetime:
local_now = datetime.now()
utc_now = datetime.now(timezone.utc)
print(local_now)
print(utc_now)
#
# Виведення:
# 2024-03-08 16:32:37.821648
# 2024-03-08 16:32:37.821648+00:00

# Щоб перетворити час з UTC в іншу часову зону, вам знадобиться визначити об'єкт timezone з відповідним зсувом.
# Наприклад, для перетворення UTC часу в час, що відповідає Східному часовому поясу США (UTC-5 годин), можна зробити наступне:

from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)

# Виведення:
# 2023-12-14 09:43:06.778253-05:00
# Щоб перетворити локальний час у час UTC, спочатку потрібно призначити
# локальному часу відповідну часову зону, а потім використати метод astimezone() для конвертації його в UTC:
from datetime import datetime, timezone, timedelta

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2024, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC

# У цьому прикладі, ми створили об'єкт datetime з часовою зоною UTC+2 (Київ) та перетворили його в час UTC. Виведення:
# 2024-03-14 10:30:00+00:00

# Стандарт ISO 8601 також підтримує часові зони. У Python це можна зробити, додавши інформацію про часову зону до об'єкта datetime:

from datetime import datetime, timezone, timedelta

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)

# Виведення:
# 2023-03-14T12:30:00+02:00
# Ці методи в datetime модулі роблять роботу з ISO форматом простою та ефективною, дозволяючи легко інтегрувати
# стандартизоване представлення дат та часу в Python-програми.

# КЛЮЧОВІ АСПЕКТИ: МЕТОДИ ДЛЯ РОБОТИ З ЧАСОВИМИ ЗОНАМИ У Python
# Отже, ми розглянули такі методи та принципи роботи з ними:
#
# Додавання інформації про часову зону до об'єкта datetime:
#  Метод astimezone використовується для перетворення об'єкта datetime з однієї часової зони в іншу. Наприклад, це
# можебути використано для конвертації часу з UTC в інші часові зони.
#

# Перетворення локального часу в час UTC:
# Спочатку призначаємо локальному часу відповідну часову зону.
# Використовуємо astimezone для конвертації в UTC. Цей підхід допомагає зручно працювати з локальним та всесвітнім часом.
#
#
# Форматування у форматі ISO 8601 із часовою зоною:
# Використовуємо isoformat для отримання рядка з об'єкта datetime у форматі ISO 8601 з часовою зоною. Це корисно для
# представлення дати та часу у єдиному стандартізованому вигляді.
#
