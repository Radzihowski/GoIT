fh = open('test1.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_four_symbols = fh.read(4)
print(first_four_symbols)

fh.close()

fh = open('test2.txt', 'w')
fh.write('Hello!')
fh.close()


fh = open('test2.txt', 'r')
all_file = fh.read()
print(all_file)
fh.close()


fh = open('test3.txt', 'w')
fh.write('Hello world')
fh.close()

fh = open('test3.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()


fh = open('test4.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test4.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()

fh = open('test5.txt', 'w')
fh.write('first line\n second line\n third line')
fh.close()

fh = open('test5.txt', 'r')
lines = fh.readlines()
print(lines)

fh.close()

