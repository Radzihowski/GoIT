# У модулі роботи з функціями ми писали функцію get_fullname для складання повного імені користувача. Виконаємо невелике
# продовження для цього завдання та напишемо функцію is_check_name, яка приймає два параметри (fullname, first_name) і
# повертає логічне значення True або False. Це результат перевірки, чи є рядок first_name префіксом рядка fullname.
# Функція is_check_name чутлива до регістру літер, тобто "Sam" і "sam" для неї різні імена.
def is_check_name(fullname, first_name):
    return fullname.find(first_name) == 0

# fullname повинно починатися з first_name, тобто бути на позиції 0
