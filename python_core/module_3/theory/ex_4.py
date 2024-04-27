from datetime import datetime, timedelta

users = [
    {"name": "Jon Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1985.01.23"},
    {"name": "Jon Doe", "birthday": "1985.01.23"}
]

prepared_users = []
for user in users:
    try:
        birthday = datetime.strptime(user["birthday"], '%Y.%m.%d').date()
        prepared_users.append({"name": user['name'], 'birthday': birthday})
    except ValueError:
        print(f'Некоректа дата народження для користувача {user["name"]}')


print(prepared_users)

# second function
def find_next_weekday(d, weekday: int):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days=days_ahead)