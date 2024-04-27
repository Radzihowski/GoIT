names = ['oleh', 'carl', 'paul', 'candymen']

normal_names = list(map(str.title, names))
print(normal_names)

print(list(map(str.title, names)))
print([i.title() for i in names])