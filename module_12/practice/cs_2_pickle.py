import pickle

d = {'some_key': 1234456778}

with open('my_dict.bin', 'wb') as file:
    pickle.dump(d, file)

d_types = pickle.dumps(d)
print(d_types)

with open('my_dict.bin', 'rb') as file:
    my_dict = pickle.load(file)

print(my_dict)
print(pickle.loads(d_types))