key = 'hello',
value = 'World'

temp = {
    'phone': 'Iphone 16',
    'clock': 'Apple Watch SE',
    'laptop': 'MacBook Pro',
    2: None,
    3.5: False,
    (4, 5): True,
    key: value,
    False: ['asdfasdfa', ['asdfasdfasdf'], ['asdfasdfasdf'], {'1': 5}]
}

a = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(a)
b = dict(a)
print(b)

d = {'phone': 'Iphone 13', 'laptop': 'MacBook Pro'}
d['phone'] = 'Iphone 15'
print(d)
d['phone1'] = 'Iphone 15'
print(d)
print(d.get('laptop3', 'Does not exist'))

d1 = {'test': 4, '5':5 }
d.update(d1)
print(d)

del d1['5']
print(d1)
d1.clear()
print(d1)
print('phone' in d)

print(d.keys())
print(d.values())
print(d)
print(d.items())