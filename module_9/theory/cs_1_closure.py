# Замикання
# Особливість існування вкладених локальних просторів імен і той факт, що вони створюються динамічно, дає змогу
# використовувати механізм замикань у Python.

message = 'Goodbye'
def outer_func(name):
    message = 'Hello'
    def inner_func(message, name):
        greeting = f'{message} {name}'
        return greeting

    return inner_func(message, name)

print(message)
print(outer_func('Oleh'))