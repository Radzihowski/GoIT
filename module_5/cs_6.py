import re
from collections import defaultdict

paragraph = """
This is a sample paragraph. It contains some words, like sample, paragraph, and words.
Let's count the frequency of each word in this paragraph!
"""

def words_frequency_counter(paragraph):
    pattern = r'\b\w+\b'
    words = re.findall(pattern, paragraph.lower())

    words_frequency = defaultdict(int)

    for word in words:
        words_frequency[word] += 1

    return words_frequency

print(words_frequency_counter(paragraph))