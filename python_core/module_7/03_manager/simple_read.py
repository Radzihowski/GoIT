from time import time
import resource

def read_file(filename):
    text_file = open(filename, 'r')
    lines = text_file.readlines()
    text_file.close()
    return lines

start = time()
data = read_file('data.txt')
diff = time() - start
print(diff)
print('Memory usage:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)