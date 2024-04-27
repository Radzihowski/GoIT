my_dict = {"name": "Alice", "age": 24, "city": "New York"}
print(my_dict["name"])

my_dict["age"] = 26
my_dict["email"] = "alice@example.com"
print(my_dict)
del my_dict["age"]
print(my_dict)

print("name" in my_dict)
print('age' in my_dict)

# Метод pop()
my_dict = {"name": "Alice", "age": 25}
age = my_dict.pop("age")
print(age)
print(my_dict)

# Метод update()
my_dict = {"name": "Alice", "age": 25}
my_dict.update({"email": "alice@newyork.com", "age": 27})
print(my_dict)

# Метод copy()
new_dict = my_dict.copy()
print(new_dict)

# Метод get()
# Метод get() використовується для безпечного отримання значення за ключем зі словника. Основна перевага цього методу
# полягає в тому, що він не викликає помилку, якщо ключ не знайдено. Натомість, якщо ключ відсутній, get() повертає
# None або інше значення, яке ви можете визначити як значення за замовчуванням.
age = new_dict.get("age")
print(age)
gender = new_dict.get("gender")
print(gender)
gender = my_dict["gender"]


# Метод clear()
my_dict.clear()
print(my_dict)