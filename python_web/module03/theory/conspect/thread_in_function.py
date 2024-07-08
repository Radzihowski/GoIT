# Потік у функції
#
# У процесі створення екземпляра класу Thread можна передати аргументу target функцію та передати їй аргументи:

from threading import Thread
from time import sleep
import logging

def example_work(delay):
    sleep(delay)
    logging.debug("Wake up!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    for i in range(5):
        thread = Thread(target=example_work, args=(i,))
        thread.start()

# Результат буде:
# Thread-1 Wake up!
# Thread-2 Wake up!
# Thread-3 Wake up!
# Thread-4 Wake up!
# Thread-5 Wake up!
# Зверніть увагу, що аргументи, які потрібно передати у функцію, передаються як кортеж args у Thread. Іменовані
# аргументи для функції можна так само передати як словник kwargs у Thread.