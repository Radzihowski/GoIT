# Нехай нам необхідно створити розсилку запрошень на якийсь захід. Повідомлення для кожного учасника однакове, нам
# необхідно міняти лише ім'я запрошеного. Цілком очевидно, що для формування такого повідомлення краще використовувати
# функцію. Створіть функцію invite_to_event, яка приймає ім'я запрошеного username і повертатиме наступний f-рядок:
#
# "Dear {username}, we have the honour to invite you to our event".

def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"

print(invite_to_event("Vasia"))