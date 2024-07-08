# Потік як функтор
#
# Є інший спосіб виконати код окремого потоку. Для цього потрібно, щоб код виконання був функтором (функцією або класом,
# який має метод __call__). Тоді об'єкт можна передати як іменований аргумент target у Thread:

from threading import Thread
from time import sleep
import logging

class UsefulClass():
    def __init__(self, delay_time):
        self.delay = delay_time

    def __call__(self):
        sleep(self.delay)
        logging.debug("Wake up!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    t2 = UsefulClass(2)
    thread = Thread(target=t2)
    thread.start()
    print("Some stuff")