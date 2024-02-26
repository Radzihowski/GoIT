# Приклад роботи функціі zip

l1 = ['a', 'b', 'c', 'd', 'e' ]
l2 = [1, 2, 3, 4, 5]
z = list(zip(l1, l2))
print(z)
print({a:b for a,b in z})