# Користувач вводить число від 0 до 100. Підрахуйте, використовуючи цикл while, суму всіх чисел від першого до введеного
# числа включно в num. Результат помістити в змінну sum.
#
# Тести будуть:
#
# Поміщати тестові значення для змінної num: 20, 10, 5, 100
#
# І чекати суми в змінній sum: 210, 55, 15, 5050

num = int(input("Enter the integer (0 to 100): "))
sum = 0
counter = 0

while counter < num:
    sum = sum + counter
    counter = counter + 1
    print(counter)

sum = sum + counter
print(sum)