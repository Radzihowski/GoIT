number = ['124', '465', '321', '55', 'abc', '211c']

def sanitaze(data):
    result = []
    for element in data:
        # if element.isdigit(): #
        try:
            result.append(int(element))
        except ValueError:
            pass
    return result

def transform_to_numbers(data):
    result = []
    for element in data:
        result.append(int(element))
    return result

san_nums = sanitaze(number)
print(sorted(san_nums))
san_nums = transform_to_numbers(san_nums)
san_nums.sort()
print(san_nums)

print('55'.isdigit())
print('c45av'.isdigit())

print(max(san_nums) - min(san_nums))
print(sum(san_nums) / len(san_nums))