print(1, oct(1), hex(1), ord('1'))

def codes_of_string(string):
    codes = dict()
    for char in string:
        if char not in codes:
            codes[char] = ord(char)
    return codes

print(codes_of_string('Hello world'))
            