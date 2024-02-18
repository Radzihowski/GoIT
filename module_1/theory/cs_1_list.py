# Створення
my_list = list()
empty_list = []
my_list = [1, 2, 3, 4, 5]
my_list = [1, "Hello", 3.14]
print(my_list)
my_list.append(4)
print(my_list)
my_list[1] = 2
print(my_list)
last = my_list.pop(1)
print(last)
print(my_list)

# Якщо виникає потреба розширити один список іншим, то використовують метод extend. Наприклад, ми маємо два списки chars
# та numbers і хочемо, щоб у список chars додалися всі елементи списку numbers.

chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers)
print(chars)
print(numbers)
chars.insert(1, 'x')
print(chars)
c_ind = chars.index('c')
print(c_ind)
chars.clear()
print(chars)
my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

words = ["banana", "apple", "cherry", "melon"]
words.sort(key=len)
print(words)  # Виведе ['apple', 'banana', 'cherry']

nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)
print(nums)

words.reverse()
print(words)