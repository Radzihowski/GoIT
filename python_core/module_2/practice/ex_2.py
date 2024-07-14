# У нас є три логічні змінні.
#
# Перша визначає статус користувача is_active, яка дорівнює True або False.
# Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
# Третя is_permission — чи дозволено доступ, теж булевого типу.
# Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.
#
# Надайте змінній access_control значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.
#
# Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.
#
# Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True.

is_active = bool(input("Is the user active? "))
is_admin = bool(input("Is the user administrator? "))
is_permission = bool(input("Does the user have access_control? "))

access = None

if is_permission == True and is_active == True or is_admin == True:
    access = True
else:
    access = False
