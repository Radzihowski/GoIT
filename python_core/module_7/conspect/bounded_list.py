class BoundedList:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        self.__data = []

    def __getitem__(self, index: int):
        return self.__data[index]

    def __setitem__(self, index: int, value: int):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value {value} must be between {self.min_value} and {self.max_value} ")
        if index >= len(self.__data): # Додати новий елемент, якщо індекс виходить за межі
            self.__data.append(value)
        else:
            self.__data[index] = value  # Замінити існуючий елемент

    def __repr__(self):
        return str(self.__data)

    def __str__(self):
        return str(self.__data)

if __name__ == '__maain__':
    temperatures = BoundedList(18, 26)

    for i, el in enumerate([20, 22, 25, 27]):
        try:
            temperatures[i] = el
        except ValueError as e:
            print(e)

    print(temperatures)