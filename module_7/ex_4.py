# Далі підуть завдання на повторення та закріплення матеріалу. Можна використовувати будь-які техніки, з якими ви
# зіткнулися у процесі навчання. І почнемо ми з функцій.
#
# У Python існує рядкова функція isdigit(). Ця функція повертає True, якщо всі символи в рядку є цифрами, і є принаймні
# один символ, інакше — False. Напишіть функцію з ім'ям is_integer, яка розширюватиме функціональність isdigit().
# При перевірці рядка необхідно ігнорувати початкові та кінцеві прогалини в рядку. Після виключення зайвих прогалин
# рядок вважається таким, що представляє ціле число, якщо:
#
# її довжина більша або дорівнює одному символу
# вона повністю складається з цифр
# передбачити виняток, що, можливо, є початковий знак "+" або "-", після якого мають йти цифри

def is_integer(s):
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] in ('-', '+'):
        s = s[1]

    return s.isdigit()



print(is_integer('Test'))
print(is_integer('123'))
print(is_integer(' 4'))
print(is_integer('6 '))
print(is_integer('+23'))
print(is_integer('-23'))