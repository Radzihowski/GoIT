# Виникає закономірне питання, навіщо, якщо результат той самий? Справа в тому, що ми можемо керувати виконанням,
# перезапуском та зупинкою роботи потоків через клас Event. Наприклад, у наступному прикладі ми перериваємо виконання
# потоку, який працює в нескінченному циклі та інакше просто ніколи не завершиться.

from threading import Thread, Event
import logging
from time import sleep


def example_work(event_for_exit: Event):
    while True:
        sleep(1)
        logging.debug("Run event work")

        if event_for_exit.is_set():
            break


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s, %(message)s")
    event = Event()
    thread = Thread(target=example_work, args=(event,))
    thread.start()

    sleep(5)
    event.set()

    logging.debug("End main program")
