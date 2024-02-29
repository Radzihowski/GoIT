# Область видимості

x = 50

def test_global():
    global x
    print(f'x is equal {x}')
    x = 2
    print(f'x was changed to {x}')

test_global()
print(x)

def outer():
    y = 'Hello World!'

    def inner_func():
        y = 'nonlocal var y'
        print(f'Inner func: {y}')

outer()