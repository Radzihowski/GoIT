class Phone:
    def __init__(self, phone) -> None:
        self.phone = phone

    @property
    def number(self):
        return self.phone

    @number.setter
    def number(self, value):
        if type(value) == int:
            self.phone = value
        if type(value) == str:
            try:
                self.phone = int(value)
            except Exception as e:
                print("Error in number")


class Age(Phone):
    pass

p = Phone("111")
print(p.number)
p.number = "22a2"
print(p.number)
