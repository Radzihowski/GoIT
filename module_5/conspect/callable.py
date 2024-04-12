from typing import Callable

def add(a:int, b:int) -> int:
    return a + b

def multiply(a:int, b:int) -> int:
    return a * b
v
def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a , b)

result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, result_multiply)