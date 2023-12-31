# Навіщо потрібен init.py
# У версіях Python до 3.3 в пакетах обов'язково потрібно було розмістити допоміжний файл __init__.py. Якщо цього не
# зробити, то Python не сприймав папку як пакет та імпортувати з такої папки нічого не міг. Зараз в цьому немає потреби,
# але часто такі файли створюються для зворотної сумісності зі старими версіями.
#
# Файл __init__.py — це службовий файл, який інтерпретатор обов'язково виконає під час першого імпорту пакету. Таким чином,
# якщо вам потрібно виконати якісь дії під час імпорту пакету, ви можете прописати їх у __init__.py.
#
# Зазвичай __init__.py — порожній і нічого не робить. Але, коли структура пакету не занадто проста і там багато модулів
# та/або пакетів, про які користувачеві знати не обов'язково, ви можете імпортувати те, що користувачеві потрібно
# у __init__.py. У такому випадку користувач зможе вже у своєму коді прописати скорочені варіанти імпортів. Наприклад,
# у пакеті utility є два пакети: useful та dummy. В кожному з них є модуль functions.py (у кожного свій).
# А в цих модулях вже є функції nice_function та not_bad відповідно. Користувачеві пакету utility необов'язково знати
# про внутрішню структуру пакету, вона зроблена для зручності розробника пакету. Розробник написав utility так, щоб
# надати користувачеві доступ до nice_function та not_bad.
#
# Якщо файл __init__.py порожній, то використання nice_function та not_bad буде виглядати якось так:
import utility

utility.useful.functions.nice_function()
utility.dummy.functions.not_bad()
# або:
from utility.useful.functions import nice_function
from utility.dummy.functions import not_bad

nice_function()
not_bad()

# Обидва варіанти припускають, що користувачеві пакету потрібно буде розібратися, де там що лежить.
#
# Якщо ж розробник подумав про користувача і __init__.py виглядає ось так:
from utility.useful.functions import nice_function
from utility.dummy.functions import not_bad

__all__ = ['nice_function', 'not_bad']
#
# Тоді можна скористатися таким імпортом:
from utility import nice_function, not_bad

nice_function()
not_bad()
#
# або:
from utility import *

nice_function()
not_bad()
#
# Зверніть увагу на константу __all__ — це список модулів або пакетів, які імпортуються, якщо у виразі from ... import
# * в кінці вказаний символ *.