# To consolidate the material, write a find_all_words function that searches for a word match in the text.
# The function returns a list of all occurrences of the word in the word parameter in the text in the form of any
# spelling, that is, for example, there are possible spellings of the word "Python" as pYthoN, pythOn, PYTHOn, etc.
# the main.py thing is that the word order is preserved, the case does not matter.
#
# Hint: the functions of the re module also take key parameter flags and we can determine case insensitivity by setting
# it to re.IGNORECASE.

import re


def find_all_words(text, word):
    result = re.findall(word, text, flags=re.IGNORECASE)
    return result



