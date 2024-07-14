# Очікування виконання потоку
#
# Коли потрібно в основному застосунку дочекатися виконання потоку, можна скористатися блокуючим методом join.

from threading import Thread
import logging
from time import sleep


def example_work(params):
    sleep(params)
    logging.debug("Wake up!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    logging.debug("Start program")
    threads = []
    for i in range(5):
        thread = Thread(target=example_work, args=(i,))
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]

    logging.debug("End program")

# У консолі ви побачите:
# MainThread Start program
# Thread-1 Wake up!
# Thread-2 Wake up!
# Thread-3 Wake up!
# Thread-4 Wake up!
# Thread-5 Wake up!
# MainThread End program

# Основний потік дочекався [el.join() for el in threads], доки завершаться всі потоки thread зі списку threads, і тільки потім вивів End program.
# Ви також можете перевірити — чи виконується потік, викликавши метод is_alive:
