# Замикання з кількома вкладеними функціями
def outer_func(variable):
    def inner_func_one(arg):
        print(f"Function one with {variable} with parameter {arg}")

    def inner_func_two(args):
        print(f"Function two with {variable} with parameter {args}")

    return inner_func_one, inner_func_two


closure = outer_func("Hello")
print(type(closure))

inner_one, inner_two = outer_func("Hello")
inner_one("Roman")
inner_two("Sergii")
