def outer_func(variable):

    def inner_func_one(arg):
        print(f"Function one with variable {variable} {arg}")

    def inner_func_two(argon):
        print(f"Function two with variable {variable} {argon}")

    return inner_func_one, inner_func_two

closure = outer_func('Hello')
print(type(closure))

inner_one, inner_two = closure

inner_one('Mike')
inner_two('Roman')