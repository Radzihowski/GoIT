# Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.
#
# Критерії надійного пароля:
#
# Довжина рядка пароля вісім символів.
# Містить хоча б одну літеру у верхньому регістрі.
# Містить хоча б одну літеру у нижньому регістрі.
# Містить хоча б одну цифру.
# Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність.
# Інакше повернути False.
def is_valid_password(password):
    flag0 = 0
    flag1 = 0
    flag2 = 0

    if len(password) != 8:
        return False
    for char in password:
        if char.isupper() == True:
            flag0 = 1
        if char.islower() == True:
            flag1 = 1
        if char.isnumeric() == True:
            flag2 = 1
    if flag0 == 1 and flag1 == 1 and flag2 == 1:
        return True
    else:
        return  False




print(is_valid_password('Password'))
print(is_valid_password('Password!'))