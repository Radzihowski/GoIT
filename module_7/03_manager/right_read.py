from time import time
import resource

def read_file_yield(filename):
    text_file = open(filename, 'r')
    while True:
        line = text.readline()
        if not line:
            text.close()
            break
        yield line

start = time()
data = read_file_yield('data.txt')
diff = time() - start
print(diff)
print('Memory usage:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)