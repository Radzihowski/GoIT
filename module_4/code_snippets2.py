cars = ['VW', 'Tesla', 'BMW', 'Toyota']
cars_copy_1 = cars.copy()
cars_copy_2 = list(cars)
cars_copy_3 = cars[:]
print(cars_copy_1)
print(cars_copy_2)
print(cars_copy_3)
print(len(cars))


a = '| '.join(cars)
print(a)
print(type(a))