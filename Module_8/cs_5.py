import random

print(random.randint(0, 100))
print(random.randrange(0, 100, 7))
print(random.choice(['black', 'white', 'red']))
print(random.choices(['black', 'white', 'red'], k=6, weights=[1, 7, 5]))

range_list = list(range(10))
print(range_list)
random.shuffle(range_list)
print(range_list)