# Pickle для збереження стану обрахунків

import pickle

def fibonacci_with_while_and_results(limit):
    try:
        # Спробуємо відновити попередній стан
        with open('fibonacci_state.pkl', 'rb') as file:
            state = pickle.load(file)
        print("Resuming calculation with previous state:", state)
    except FileNotFoundError:
        # Якщо файл не знайдено, починаємо з початку
        print("Starting a new calculation...")
        state = {'current': 0, 'next': 1, 'results': []}

    while state['current'] < limit:
        # Додаємо поточне число до результатів
        state['results'].append(state['current'])

        # Обчислюємо наступне число Фібоначчі
        new_value = state['current'] + state['next']

        # Оновлюємо стан
        state['current'], state['next'] = state['next'], new_value

        # Збереження стану у файл за допомогою pickle
        with open('fibonacci_state.pkl', 'wb') as file:
            pickle.dump(state, file)

    def filter_result(fib_number):
        return fib_number <= limit


    print("Calculation completed.")
    print("Final calculation state:", state)
    return list(filter(filter_result, state['results']))[-1]

# Викликайте функцію для роботи з while loop та отримання результатів
fibonacci_results = fibonacci_with_while_and_results(100)

# Виведення результатів
print("Results:", fibonacci_results)