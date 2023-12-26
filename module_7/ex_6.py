# Всі ви, можливо, стикалися з ребусами "Знайди слово". Вони існують як текстові варіанти, так і як програми для мобільних
# додатків. Нагадаємо коротко суть ребуса. У великому квадраті з набором букв необхідно знайти слово по горизонталі та
# інколи по вертикалі.
#
# game
# Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) для знаходження слова, що шукається
#в рядку ребуса.
#
# Параметри функції:
#
# riddle - рядок із зашифрованим словом.
# word_length – довжина зашифрованого слова.
# start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
# reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване у
# зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
# Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.
import re
def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        pattern = f'\w{{{word_length - 1}}}{start_letter}'
        found_data = re.search(pattern, riddle)
        if found_data != None:
            raw_result = found_data.group()
            result = raw_result[::-1]
            return result
    pattern = f'{start_letter}\w{{{word_length - 1}}}'
    found_data = re.search(pattern, riddle)
    if found_data != None:
        result = found_data.group()
        return result
    else:
        return ""

print(solve_riddle("mi1rewopret", 5, 'p', True))






