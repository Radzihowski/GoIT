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

print(find_stop_words(text, 'frequency', is_space=True))

print(text.split())