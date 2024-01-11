def foo(value):
    return value + 2

def baz(value):
    return  value * 2

def compoze(func_one, func_two):
    return lambda value: func_one(func_two(value))

foobaz = compoze(foo, baz)

print(foo(3), baz(3), foobaz(3))
print(foo((baz(3))))
print(baz(foo(3)))