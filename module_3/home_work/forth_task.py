# Четверте завдання

# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати.

# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

# Вимоги до завдання:
# - Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
# - Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
# - Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').
#
# Рекомендації для виконання:
# - Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків у об'єкти datetime. Конвертуйте дату народження із рядка у datetime об'єкт - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
# - Визначте поточну дату системи за допомогою datetime.today().date().
# - Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
# - Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
# - Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
# - Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
# - Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
# - Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань.
#
# Критерії оцінювання:
# Актуальність та коректність визначення днів народження на 7 днів вперед.
# Правильність обробки випадків, коли дні народження припадають на вихідні.
# Читабельність та структурованість коду.
#
# Приклад:
# Припустимо, у вас є список users:
# users = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]
#
# Використання функції get_upcoming_birthdays:
# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)
#
# Якщо сьогодні 2024.01.22 результатом може бути:
# [
#     {'name': 'John Doe', 'congratulation_date': '2024.01.23'},
#     {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
# ]
#

# Цей список містить інформацію про те, кого і коли потрібно привітати з днем народження на поточному тижні.

# Формат здачі ДЗ
# 📌Розмістіть файли з розв'язанням у репозиторії goit-algo-hw-03, та прикріпіть лінки до них у відповідь на домашнє завдання.
# Формат оцінювання
# Залік/незалік

from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.15"},
    {"name": "John David", "birthday": "1985.03.17"},
    {"name": "John Siena", "birthday": "1980.06.22"},
    {"name": "Jack Sparrow", "birthday": "1985.02.05"},
    {"name": "Jane Ohara", "birthday": "1985.01.27"},
    {"name": "Jane Smith", "birthday": "1990.03.20"}
]

def get_upcoming_birthdays(users):
    prepared_users = []
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
            prepared_users.append({"name": user['name'], 'birthday': birthday})
        except ValueError:
            print(f'Некоректа дата народження для користувача {user["name"]}')

    # print(prepared_users)

    def find_next_weekday(d, weekday: int):
        """
        Функція для знаходження заданного дня тиждня після заданоі дати
        :param d: datatime.date - початкова дата
        :param weekday: int - день тиждня від 0(понеділок) до 6(неділя)
        :return: буде перевіряти цю різницю
        """

        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:  # Якщо день народження вже минув
            days_ahead += 7
        return d + timedelta(days=days_ahead)

    days = 7
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in prepared_users:
        birthday_this_year = user["birthday"].replace(year=today.year)  # 1985 -> 2024

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:  # Субота і Неділя
                birthday_this_year = find_next_weekday(birthday_this_year, 0)  # це буде Понеділок

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays

print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
