# 1
fh = open('test6.txt', 'w+')
fh.write('hello!')

fh.seek(1)
third = fh.read(1)
print(third)

fh.close()

# 2
fh = open('test6.txt', 'w+')
fh.write('hello!')

position = fh.tell()
print(position)

fh.seek(1)
position = fh.tell()
print(position)

fh.read(2)
position = fh.tell()
print(position)

fh.close()


