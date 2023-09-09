# Перепишіть приклад із теорії, але для додатного числа перевіряйте — парне воно чи ні. Таким чином після перевірок змінна
# result повинна містити одне з чотирьох значень:
#
# "Positive even number"
# "Positive odd number"
# "Negative number"
# "It is zero"
# Підказка: перевірка на парність виконується порівнянням залишку від поділу на 2 з 0 або 1. Нагадаємо, залишок від
# ділення можна отримати після операції %

num = int(input("Enter a number: "))

if num > 0:
    if  num % 2 != 0:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"
