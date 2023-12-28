# Виконати симулювання 1000 викидань гральних кісток. Порівняти очікуваний результат імовірності випадання з реальним. Очікуваний відсоток
#
# 2: 2,78
# 3: 5,56
# 4: 8,33
# 5: 11,11
# 6: 13,89
# 7: 16,67
# 8: 13,89
# 9: 11,11
# 10: 8,33
# 11: 5,56
# 12: 2,78
# результат зберегти в текстовий файл формату md, у вигляді таблиці

import random

NUMBER_ATTEMPTS = 1000

expected_outcome = {
    "2": 2.78,
    "3": 5.56,
    "4": 8.33,
    "5": 11.11,
    "6": 13.89,
    "7": 16.67,
    "8": 13.89,
    "9": 11.11,
    "10": 8.33,
    "11": 5.56,
    "12": 2.78
}

def dice_roll():
    return  random.randint(1, 6)

def experiment():
    value_obtained = {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0
    }

    for el in random(NUMBER_ATTEMPTS):
        # roll_one = dice_roll()
        # roll_two = dice_roll()
        # sum_roll = roll_one + roll_two
        # current = value_obtained.get(str(sum_roll))
        # value_obtained.update({str(sum_roll): current + 1})
        value_obtained[str(dice_roll() + dice_roll())] += 1

    for key, value in value_obtained.items():
        value_obtained[key] = round(value / NUMBER_ATTEMPTS * 100, 2)

    return value_obtained

print(experiment())