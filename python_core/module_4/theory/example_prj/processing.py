# Файл processing.py міститиме логіку обробки даних: обчислення середньої, мінімальної, максимальної та медіанної температури.

def calculate_statistics(temperatures: list[float]) -> dict:
    if not temperatures:
        return None

    min_temp = min(temperatures)
    max_temp = max(temperatures)
    avg_temp = sum(temperatures) / len(temperatures)
    median_temp = calculate_median(temperatures)

    return {
        "min": min_temp,
        "max": max_temp,
        "average": avg_temp,
        "median": median_temp
    }


def calculate_median(temperatures: list[float]) -> float:
    temperatures.sort()
    n = len(temperatures)
    mid = n // 2
    if n % 2 == 0:
        return (temperatures[mid-1] + temperatures[mid]) / 2
    else:
        return temperatures[mid]

# Тут все досить зрозуміло: для розрахунку середньої, мінімальної та максимальної температури ми використовуємо вбудовані
# функції Python. Функція min повертає найменше значення з набору або з послідовності. Це може бути список, кортеж,
# множина чи будь-який інший ітерований об'єкт. На відміну від min, функція max повертає найбільше значення з набору
# даних або послідовності. Функція sum використовується для обчислення суми елементів у послідовності, зазвичай чисел

# Функція calculate_median обчислює медіану для вхідного списку чисел temperatures.
#
# Пояснимо, як вона працює:
# Спочатку список temperatures сортується за зростанням.
# Потім обчислюється довжина списку n.
# Індекс середини списку визначається як mid = n // 2.
# Якщо кількість елементів у списку парна n % 2 == 0, медіаною буде середнє арифметичне двох середніх елементів, тобто
# (temperatures[mid - 1] + temperatures[mid]) / 2.
# Якщо кількість елементів у списку непарна, медіаною буде елемент у центрі списку, тобто temperatures[mid].
#
# Головний файл main.py використовує функції з data.py та processing.py для виконання завдання.