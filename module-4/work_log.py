a = list('Hello world')
print(a)

m = '13/10/2023'
m_1 = m.split('/')
print(m_1)

cars = ['VW', 'Tesla', 'BMW', 'Toyota']
print(cars)
a = ', '.join(cars)
print(a)
a = ' | '.join(cars)
print(a)
print(type(a))

print(cars)
print(cars[0])
print(cars[3])
print(cars[-1])
print(cars.index('Tesla'))

test = [ 5, 12.5, True]

all_info = [cars, 'test', test]
print(all_info)
print(all_info[0])
print(all_info[1])
print(all_info[2])
print(all_info[0][3])

cars1 = ['VW', 'Tesla', 'BMW', 'Toyota']
cars1[0] = 'Ford'
print(cars1)

cars2 = ['VW', 'Tesla', 'BMW', 'Toyota']
cars2.append('Opel')
print(cars2)
cars2.insert(3, 'AMG')
print(cars2)