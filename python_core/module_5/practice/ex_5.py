# Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії. Тепер у списку
# можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .
#
# Компанія працює з наступними країнами
#
# Країна	Код ISO	Префікс
# Japan     JP	    +81
# Singapore	SG	    +65
# Taiwan	TW	    +886
# Ukraine	UA	    +380
# Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних
# номерів.
#
# Напишіть функцію get_phone_numbers_for_сountries, яка буде:
#
# Приймати список телефонних номерів.
# Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
# Сортувати телефонні номери за вказаними у таблиці країнами.
# Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
# {
#     "UA": [<тут список телефонів>],
#     "JP": [<тут список телефонів>],
#     "TW": [<тут список телефонів>],
#     "SG": [<тут список телефонів>]
# }
# Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    phone_number_per_country = {"UA": [], "JP": [], "TW": [], "SG": []}

    if len(list_phones) == 0:
        return phone_number_per_country

    for element in list_phones:
        tel_number = sanitize_phone_number(element)

        if tel_number.startswith("81"):
            phone_number_per_country.get('JP').append(tel_number)
            continue
        elif tel_number.starstwith("65"):
            phone_number_per_country.get("SG").append(tel_number)
            continue
        elif tel_number.starstwith("886"):
            phone_number_per_country.get("TW").append(tel_number)
            continue
        else:
            phone_number_per_country.get("UA").append(tel_number)

    return phone_number_per_country