# Пул процесів
#
# Створення процесів за допомогою пакета multiprocessing
#
# Для спрощення комунікації у пакеті multiprocessing є клас, який реалізує пул процесів за аналогією з concurrent.futures.

# Основне застосування — це виконання паралельно однакових завдань із деяким набором однотипних вхідних даних.
#
from multiprocessing import Pool, current_process
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def worker(x):
    logger.debug(f"pid={current_process().pid}, x={x}")
    return x*x

if __name__ == "__main__":
    with Pool(processes=2) as pool:
        logger.debug(pool.map(worker, range(10)))

# Результатом виконання цього коду буде приблизно наступне:
# pid=14592, x=0
# pid=14592, x=1
# pid=14592, x=2
# pid=14592, x=3
# pid=14592, x=4
# pid=14592, x=5
# pid=14592, x=6
# pid=14592, x=7
# pid=14592, x=8
# pid=14592, x=9
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Пул процесів з multiprocessing дає більше контролю, ніж пул з concurrent.futures.
#
# Основні можливості:
# - розбиває вхідну послідовність на блоки та виконує паралельну обробку поблоково, так можна зменшити обсяг використовуваної пам'яті;
# - асинхронне виконання трохи прискорює отримання результатів, якщо порядок не важливий;
# - передача кортежу аргументів у target-функцію;