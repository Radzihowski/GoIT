class compValue:
    def __init__(self, a) -> None:
        self.value = a

    def __cmp__(self, other):
        return self.value-other.value

    def __eq__(self, __value: object) -> bool:
        return self.value==__value.value


A = compValue(3)
B = compValue(3)
print(A == B)
