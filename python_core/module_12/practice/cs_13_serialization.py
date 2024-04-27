import pickle

class TextReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, encoding='utf-8')
        self.line_idx = 0

    def readline(self):
        self.line_idx += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return '%i: %s' % (self.line_idx, line)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['file']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        file = open(self.filename, encoding='utf-8')
        for _ in range(self.line_idx):
            file.readline()
        self.file = file


reader = TextReader('lines.txt')
print(reader.readline())
print(reader.readline())
new_reader = pickle.loads(pickle.dumps(reader))
print(new_reader.readline())
print(reader.readline())
print(reader.readline())
print(new_reader.readline())
print(new_reader.readline())
print(new_reader.readline())
print(new_reader.readline())
print(reader.readline())