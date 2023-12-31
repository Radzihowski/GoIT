# datetime
# Клас datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - комбінація дати і часу.
#
# Обов'язкові аргументи:
#
# datetime.MINYEAR (1) ≤ year ≤ datetime.MAXYEAR (9999)
#
# 1 ≤ month ≤ 12
#
# 1 ≤ day ≤ кількість днів у даному місяці та році
#
# Необов'язкові:
#
# 0 ≤ minute < 60 0 ≤ second < 60 0 ≤ microsecond < 1000000
#
# Методи класу datetime:
#
# datetime.today() - об'єкт datetime з поточної дати і часу. Працює так само, як і datetime.now() зі значенням tz=None.
#
# datetime.fromtimestamp(timestamp) - дата зі стандартного подання часу.
#
# datetime.fromordinal(ordinal) - дата з числа, що являє собою кількість днів, що минули з 01.01.1970.
#
# datetime.now(tz=None) - об'єкт datetime з поточної дати і часу.
#
# datetime.combine(date, time) - об'єкт datetime з комбінації об'єктів date і time.
#
# datetime.strptime(date_string, format) - перетворює рядок у datetime (так само, як і функція strptime з модуля time).
#
# datetime.strftime(format) - див. функцію strftime з модуля time.
#
# datetime.date() - об'єкт дати (з відсіканням часу).
#
# datetime.time() - об'єкт часу (з відсіканням дати).
#
# datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]) - повертає новий об'єкт
# datetime зі зміненими атрибутами.
#
# datetime.timetuple() - повертає struct_time з datetime.
#
# datetime.toordinal() - кількість днів, що минули з 01.01.1970.
#
# datetime.timestamp() - повертає час у секундах з початку епохи.
#
# datetime.weekday() - день тижня у вигляді числа, понеділок - 0, неділя - 6.
#
# datetime.isoweekday() - день тижня у вигляді числа, понеділок - 1, неділя - 7.
#
# datetime.isocalendar() - кортеж (рік у форматі ISO, ISO номер тижня, ISO день тижня).
#
# datetime.isoformat(sep='T') - красивий рядок вигляду "YYYYY-MM-DDTHH:MM:SS.mmmmmm" або, якщо microsecond == 0, "YYYY-MM-DDTHH:MM:SS"
#
# datetime.ctime([сек]) - перетворює час, виражений у секундах від початку епохи, у рядок виду "Thu Sep 27 16:42:37 2012".\
#
# Нижче наведено коди символів для форматування дати та часу:-
#
# %d: Повертає день місяця, від 1 до 31.
# %m: Повертає місяць року, від 1 до 12.
# %Y: Повертає рік у чотиризначному форматі (рік зі століттям), наприклад, 2021.
# %y: Повертає рік у двозначному форматі (рік без століття). наприклад, 19, 20, 21
# %A: Повертає повну назву дня тижня. Наприклад, понеділок, вівторок
# %a: Повертає коротку назву дня тижня (перші три символи). Наприклад, понеділок, вівторок
# %B: Повертає повну назву місяця. Наприклад, червень, березень
# %b: Повертає коротку назву місяця (перші три символи). Наприклад, березень, червень
# %H: Повертає годину. від 01 до 23.
# I: Повертає годину у 12-годинному форматі. від 01 до 12.
# %M: Повертає хвилину, від 00 до 59.
# %S: Повертає секунду, від 00 до 59.
# %f: Повертає мікросекунди від 000000 до 999999
# %p: Повернути час у форматі AM/PM
# %c: Повертає відповідне представлення дати і часу у локалі
# %x: Повертає відповідне представлення дати для даної місцевості
# %X: Повертає відповідне представлення часу в локалі
# %z: Повертає зміщення UTC у вигляді ±HHMM[SS[.ffffff]] (порожній рядок, якщо об'єкт наївний).
# %Z: Повертає назву часового поясу (порожній рядок, якщо об'єкт наївний).
# %j: Повертає день року від 01 до 366
# %w: Повертає день тижня у вигляді десяткового числа, де 0 - неділя, а 6 - субота.
# %U: Повертає номер тижня року (неділя - перший день тижня) від 00 до 53
# %W: Повертає номер тижня року (понеділок як перший день тижня) від 00 до 53


from datetime import datetime

current_day = datetime.now()
print(current_day)

print(current_day.date())
print(current_day.time())
print(current_day.year, current_day.month, current_day.hour, sep='\t')