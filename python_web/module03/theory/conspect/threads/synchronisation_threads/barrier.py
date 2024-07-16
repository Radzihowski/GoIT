# Barrier
#
# Останній примітив синхронізації, який ми розглянемо в Python — це бар'єр Barrier. Він дозволяє задати умову, щоб
# кілька потоків продовжили роботу лише після того, як задане число потоків добереться у виконанні коду до цього "бар'єру".
#
# Використовується, коли вам потрібно, щоб робота застосунку продовжилася лише після того, як усі потоки зроблять якусь
# частину своєї роботи та дійдуть до деякої точки, з якою можна знову продовжувати.
#
# Розглянемо наступний приклад:

from random import randint
from threading import Thread, Barrier
import logging
from time import sleep, ctime


def worker(barrier: Barrier):
    logging.debug(f"Start thread: {ctime()}")
    sleep(randint(1, 3))  # Simulate some work
    r = barrier.wait()
    logging.debug(f"count {r}")
    logging.debug(f"Barrier overcome: {ctime()}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    barrier = Barrier(5)

    for num in range(10):
        thread = Thread(name=f"Th-{num}", target=worker, args=(barrier,))
        thread.start()

# Потік може дістатися бар'єру і чекати його за допомогою функції wait(). Це блокуючий виклик, який повернеться, коли
# решта потоків (попередньо налаштована кількість barrier = Barrier(5)) дістануться бар'єру.
#
# Функція очікування wait() повертає ціле число, яка вказує на кількість учасників, що залишилися до бар'єру. Якщо
# потік був останнім, що прибув, то повернене значення буде нульовим.
#
# Як бачимо в нашому прикладі, спочатку виконалися потоки:
# Th-4 Barrier overcome: Tue Oct 18 12:13:22 2022
# Th-0 Barrier overcome: Tue Oct 18 12:13:22 2022
# Th-1 Barrier overcome: Tue Oct 18 12:13:22 2022
# Th-6 Barrier overcome: Tue Oct 18 12:13:22 2022
# Th-3 Barrier overcome: Tue Oct 18 12:13:22 2022
#
# А потім наступні п'ять потоків
# Th-7 Barrier overcome: Tue Oct 18 12:13:24 2022
# Th-2 Barrier overcome: Tue Oct 18 12:13:24 2022
# Th-9 Barrier overcome: Tue Oct 18 12:13:24 2022
# Th-8 Barrier overcome: Tue Oct 18 12:13:24 2022
# Th-5 Barrier overcome: Tue Oct 18 12:13:24 2022

# Головна вимога, щоб кількість потоків, що запускаються, в нашому випадку 10 - range(10), була кратною кількості
# бар'єру, у нашому випадку 5 - Barrier(5).
