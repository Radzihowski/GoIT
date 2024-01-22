# Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів:
# [\n, \f, \r, \t, \v]
#
# Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:
#
# 'Alex\nKdfe23\t\f\v.\r'
# 'Al\nKdfe23\t\v.\r'

def real_len(text):
    new_text = text.replace('\n', '')
    new_text = new_text.replace('\t', '')
    new_text = new_text.replace('\v', '')
    new_text = new_text.replace('\r', '')
    new_text = new_text.replace('\f', '')
    return len(new_text)

print(real_len('Alex\nKdfe23\t\f\v.\r'))
print(real_len('Al\nKdfe23\t\v.\r'))




