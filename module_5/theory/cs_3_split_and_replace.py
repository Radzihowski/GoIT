# str.split(): Розбиває строку на список підстрок за допомогою роздільника (пробіл - за замовчуванням) і повертає список.
# str.replace(old, new): Заміняє всі входження old на new у строкі і повертає нову строку.

# Перевірити чи строка містить певні слова або частини цих слів
text = """
This is a sample paragraph. It contains some words, like sample, paragraph, and words.
Let's count the frequency of each word in this paragraph!
"""


def find_stop_words(text, stop_word, is_space=False):
    if is_space:
        new_text = text.split(' ')
        for word in new_text:
            word = word.replace(',', '').replace('.', '').replace('!', '').replace('\n', '')
            if stop_word.lower() in word.lower() and len(stop_word) == len(word):
                return True
    else:
        if stop_word.lower() in text.lower():
            return True

    return False


# new_text = text.split(' ')
# print(new_text)

print(find_stop_words(text, 'Frequen', is_space=True))
print(find_stop_words(text, 'frequency', is_space=True))
print(find_stop_words(text, 'Frequen', is_space=False))
print(find_stop_words(text, 'frequency', is_space=False))

text = """
This is a sample paragraph. It contains some words, like sample, paragraph, and words.
Let's count the frequency of each word in this paragraph!
"""


def find_stop_words(text, stop_word, is_space=False):
    if is_space:
        new_text = text.split(' ')
        for word in new_text:
            word = word.replace(',', '').replace('.', '').replace('!', '').replace('\n', '')
            if stop_word.lower() in word.lower() and len(stop_word) == len(word):
                return True

    else:
        if stop_word.lower() in text.lower():
            return True
    return False


def find_stop_words(text, stop_word, is_space=False):
    if is_space:
        new_text = text.split(' ')
        for word in new_text:
            word = word.replace(',', '').replace('.', '').replace('!', '').replace('\n', '')
            return stop_word.lower() in word.lower() and len(stop_word) == len(word)
    else:
        return stop_word.lower() in text.lower()


# Алтернатива один
def find_stop_words(text, stop_word, space_around=False):
    text = text.lower().replace(',', '').replace('.', '')
    stop_word = stop_word.lower()
    if space_around:
        if (' ' + stop_word + ' ') in text or text.startswith(stop_word + ' ') or text.endswith(' ' + stop_word):
            return True
    else:
        if stop_word in text:
            return True
    return False


# Алтернатива два
def find_stop_words(text, stop_word, space_around=False):
    new_text = text.split(' ')
    stop_word = stop_word.lower()
    for word in new_text:
        if space_around:
            word = word.replace(',', '').replace('.', '')
            if stop_word in word and len(word) == len(stop_word):
                return True
        else:
            if stop_word in word:
                return True
    else:
        return False


print(find_stop_words(text, 'Frequency', is_space=True))
