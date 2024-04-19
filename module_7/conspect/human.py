class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age

    def say_hello(self) -> str:
        return f"Hello! I am {self.name}"

bill = Human('Bill')
print(bill.say_hello())
print(bill.age)

jill = Human("Jill")
print(jill.say_hello())
print(jill.age)

