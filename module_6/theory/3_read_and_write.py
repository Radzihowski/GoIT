# Читання та запис у файл
# Для запису у файл використовується метод write у дескриптора fh. Цей метод повертає кількість записаних у файл символів.
# Парний до нього метод — це метод read, який дозволяє прочитати деяку кількість символів із файлу.

fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'

fh.close()

# В цьому прикладі ми відкрили файл для читання та запису. Записали у файл рядок 'hello!' та прочитали перші два символи із файлу за допомогою методу read, вказавши у якості аргументу двійку.
# Щоб повернути курсор на початок файлу, викликали метод seek та передали йому позицію, куди потрібно переміститися (0).
# Щоб прочитати увесь вміст файлу за раз, можна викликати метод read без аргументів:

fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
all_file = fh.read()
print(all_file)  # 'hello!'

fh.close()

# Доки файловий дескриптор не закритий, ви можете читати із нього частинами, продовжуючи читання з того самого місця, на якому зупинилися:

fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()


# В цьому прикладі у циклі ми зчитували та виводили у консоль вміст файлу по одному символу за раз. В результаті ви отримаєте у консолі:

# h
# e
# l
# l
# o
# !

# Ще є зручний спосіб читати файл порядково, по одному рядку за раз, для цього можна скористатися методом readline:

fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()


# В консолі буде виведення:

#
#
# first line
#
# second line
#
# third line
#
#
# Та аналогічний метод readlines, який читає увесь файл повністю, але повертає список рядків, де елемент списку — це один рядок



fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
lines = fh.readlines()
print(lines)

fh.close()


# Виведення у консолі буде:
#
#
#
# ['first line\n', 'second line\n', 'third line']
#
#
# Зверніть увагу, що всі методи, які читають файли порядково, не опускають (видаляють) символ перенесення рядка.


