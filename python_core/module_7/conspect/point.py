class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

original_point = Point(2, 3)
print(repr(original_point))

new_point = eval(repr(original_point))
print(new_point)

