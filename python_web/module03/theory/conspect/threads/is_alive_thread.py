# Ви також можете перевірити — чи виконується потік, викликавши метод is_alive:

from threading import Thread
from time import sleep
import logging


class UsefulClass:
    def __init__(self, second_num):
        self.delay = second_num

    def __call__(self):
        sleep(self.delay)
        logging.debug("Wake up!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    t2 = UsefulClass(1)
    thread = Thread(target=t2)
    thread_locking = Thread(target=t2)

    thread.start()
    print(thread.is_alive(), thread_locking.is_alive())
    thread_locking.start()
    thread.join()
    thread_locking.join()
    print(thread.is_alive(), thread_locking.is_alive())
    print("After all...")

# True False
# Thread - 2 Wake up!
# Thread - 1 Wake up!
# False False
# After all...

# Це може бути корисним, якщо ви хочете перевіряти стан потоку самостійно і не блокувати застосунок в очікуванні завершення.
