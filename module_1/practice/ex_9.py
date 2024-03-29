# Повернімося до завдання з розрахунку площі. Створіть програму на Python, яка розраховує площу кімнати, перетворюючи
# рядкові значення довжини та ширини на числа, та формує інформативне повідомлення про результат.
#
# Задачі:
#
# Оголосіть змінні length та width з рядковими значеннями довжини та ширини кімнати. Задайте їм значення "2.75" та "1.75".
# Перетворіть рядкові значення length та width на дійсні числа (тип float) при розрахунку площі.
# Розрахуйте площу кімнати area як добуток перетворених значень довжини та ширини.
# Створіть змінну show, яка міститиме інформативний рядок із шаблоном: 'With width <значення ширини> and
# length < значення довжини> of the room, its area is equal to <значення площі>'.
# Очікуваний результат:
#
# Програма повинна зберегти в змінну show інформативний рядок про розміри кімнати та її площу, використовуючи
# перетворення з рядкових у числові значення довжини та ширини.
#
# Підказки:
#
# Використовуйте функцію float() для перетворення рядкових значень у дійсні числа.
# У змінній show переконайтеся, що відображені коректні розміри та площа кімнати.

length = "2.75"
width = "1.75"
area = float(length) * float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"