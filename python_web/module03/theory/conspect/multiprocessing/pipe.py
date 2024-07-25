# Pipe (канал)
#
# Механізм каналів реалізований поверх сокетів (мережеві інтерфейси) і дає зручніший інтерфейс. Канали доступні на всіх
# POSIX системах (Linux, Mac OS, FreeBSD, Unix).
#
# Канал — пара об'єктів — кінці каналу. Ви можете асинхронно писати в канал (надсилати повідомлення) та читати з каналу
# (отримувати повідомлення на іншому кінці). Повідомлень у каналі може бути більше одного одночасно і порядок
# повідомлень гарантується. Канали реалізують обмін між двома процесами, не можна використовувати один і той самий
# кінець каналу в кількох процесах.
#
# Клас Pipe модуля multiprocessing повертає парний кортеж (conn1, conn2), що складається з об'єктів Connection, що
# представляють кінці одного каналу.
#
# Клас Pipe приймає аргумент дуплекс duplex, який за замовчуванням дорівнює True. Тоді канал є двоспрямованим, якщо ж
# duplex=False, тоді канал є односпрямованим і тоді conn1 використовується для приймання повідомлень, а conn2 для
# надсилання повідомлень.
#
# Об'єкти conn1 та conn2 мають ряд методів, основні це:
# send — відправляє об'єкт на інший кінець з'єднання
# recv — повертає об'єкт, відправлений з іншого кінця з'єднання
# close закриває з'єднання
#
# Давайте розглянемо приклад реалізації каналу в Python за допомогою класу Pipe.

import logging
import sys
from multiprocessing import Pipe, Process, current_process
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

recipient1, sender1 = Pipe()  # Creates a pair of connection objects (recipient1 and sender1) for inter-process communication.
recipient2, sender2 = Pipe()  # Creates another pair of connection objects (recipient2 and sender2).


def worker(pipe: Pipe):
    name = current_process().name
    logger.debug(f'{name} started...')
    val = pipe.recv()
    logger.debug(val ** 2)
    sys.exit(0)


if __name__ == '__main__':
    w1 = Process(target=worker, args=(recipient1,))
    w2 = Process(target=worker, args=(recipient2,))

    w1.start()
    w2.start()

    sender1.send(8)
    sleep(1)
    sender2.send(16)

# У цьому прикладі ми пишемо в канали з батьківського процесу sender1.send(8) та sender2.send(16), а читаємо з дочірніх
# pipe.recv() всередині функції worker.
#
# Виведення:
# Process-1 started...
# 64
# Process-2 started...
# 256

# У канал можна відправити будь-який тип даних, який можна перетворити на byte-рядок за допомогою pickle. Не можна
# надсилати функції або інші об'єкти, які не серіалізуються.
