import mymodule

print(mymodule.say_hello("World"))

from mymodule import say_hello
print(say_hello("World 2"))

from mymodule import say_hello as greeting
print(greeting('World3'))

print(dir())
print(greeting("World"))