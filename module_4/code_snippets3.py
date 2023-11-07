a = 'Iphone 15', 'Watch 8', 'MacBook', 'test'
print(a)
print(type(a))

iphone, clock, laptop, *_ = a
*_, laptop, test = a
print(clock)

b = ['Iphone 15', 'Watch 8', 'MacBook', 'test']
b_new = tuple(b)
print(b_new)
print(b_new[1])