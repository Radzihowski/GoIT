"""
Метод: sub => re.sub(pattern, repl, string, count=0, flags=0); Заміняє елемент
"""

import re

string = "The best language is Java and Java"
print(re.sub(r'java', 'Python', string, 1, flags=re.IGNORECASE))
# print(re.sub(r'java', 'Python', string, 1))
