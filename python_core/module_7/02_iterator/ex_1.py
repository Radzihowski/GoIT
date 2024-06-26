# Ітератор
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >=  len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_iter = MyIterator([1, 2, 3, 4, 5])
for item in my_iter:
    print(item)
print('=' * 10)
# Генератор
def my_generator(data):
    for item in data:
        yield item

my_gen = my_generator([1, 2, 3, 4, 5])
for item in my_gen:
    print(item)