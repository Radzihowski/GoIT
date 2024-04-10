# Файл data.py відповідатиме за завантаження та первинну обробку даних.
def load_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return file.readlines()

def clean_data(temperature_data: list[str]) -> list[float]:
    return [float(temp.strip()) for temp in temperature_data if temp.strip()]

# Функція load_data читає дані з файлу та повертає список рядків. Функція clean_data виконує очищення даних та перетворює
# рядки в числа і відкидає порожні рядки.
#
# Файл processing.py міститиме логіку обробки даних: обчислення середньої, мінімальної, максимальної та медіанної температури.