# Напишіть програму, яка для двох додатних цілих чисел знаходить НСД.
#
# Примітка: Для умови циклу в пункті 3 необхідно пам'ятати, що цикл while виконується за умови True, а наш цикл повинен
# закінчитися, тільки якщо gcd поділив обидва числа без залишку.

first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = min(first, second)

while not (first % gcd == 0 and second % gcd == 0):
    gcd = gcd - 1
    print(gcd)


