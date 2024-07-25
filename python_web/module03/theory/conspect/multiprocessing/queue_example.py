# Черги завдань
# Окремий механізм обміну даними між процесами — це черги. Черга дозволяє "покласти" дані для обробки одним із
# "працівників" і потім проконтролювати, коли "працівник" завершив обробку. Черги — це засіб комунікації між одним
# відправником, найчастіше його називають master, та будь-якою кількістю одержувачів повідомлень, часто їх називають
# slave або у нейтральнішому тоні — worker.
#
# Об'єктів у черзі може бути більше одного. Черга може бути обмежена за розміром, якщо це потрібно. Черга гарантує
# порядок повідомлень та неможливість отримання одного повідомлення кількома одержувачами.
#
# Черги в Python реалізовані у класах Queue та JoinableQueue:

from multiprocessing import Queue, Process, current_process
from time import sleep
import sys
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

q = Queue()


def worker(queue: Queue):
    name = current_process().name
    logger.debug(f'{name} started...')
    val = queue.get()
    logger.debug(f'{name} {val**2}')
    sys.exit(0)


if __name__ == '__main__':
    w1 = Process(target=worker, args=(q, ))
    w2 = Process(target=worker, args=(q, ))

    w1.start()
    w2.start()

    q.put(8)
    sleep(1)
    q.put(16)

# Виведення:
# Process-1 started...
# Process-1 64
# Process-2 started...
# Process-2 256
# У цьому прикладі ми створили два процеси w1 та w2, які беруть із черги q собі завдання і виконують їх. Наш основний
# процес, що виконує роль master, кладе завдання у чергу q, але ніяк не контролює їх виконання, а процеси worker читають
# повідомлення з черги та завершуються.
