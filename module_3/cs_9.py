# Задача 9
# Програма загадує ціле число від 0 до n, де n - переданий у функцію параметр. Користувач намагається відгадати загадане
# число. Якщо користувач назвав занадто велике число, функція повинна відповісти 'Smaller'. Якщо він назвав занадто
# маленьке число, функція повинна 'Larger'. Якщо користувач вгадав число, функція повинна відповісти 'You won!' і
# говорить за скільки спроб він вгадав
from random import randint


def predict_number(number):
    count = 0
    goal = randint(0, number)

    while True:
        user_input = int(input(f"Guess the number from 0 to {number}: "))
        count += 1

        if user_input > goal:
            print("Smaller")
        elif user_input < goal:
            print("Greater")
        else:
            print(f"you win! Number of attempts {count}")
            break


predict_number(10)
