# Вимогливіший до ресурсів, але й зручніший у використанні механізм обміну даними між процесами — це Менеджер ресурсів.
# Основна перевага — можливість працювати по всій мережі та реалізувати розподілені обчислення між кількома комп'ютерами
# в одній мережі, реалізація Python-like списків та словників.
#
# Недоліки:
# Необхідність синхронізувати доступ до загальних ресурсів;
# Обмеження типів, що підтримуються;
# Складне API.
#
# Розглянемо наступний приклад:
#
import logging
from multiprocessing import Process, Manager, current_process
from random import randint
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(delay, val: Manager):
    name = current_process().name
    logger.debug(f'Started: {name}')
    sleep(delay)
    val[name] = current_process().pid
    logger.debug(f'Done: {name}')


if __name__ == '__main__':
    with Manager() as manager:
        m = manager.dict()
        processes = []
        for i in range(5):
            pr = Process(target=worker, args=(randint(1, 3), m))
            pr.start()
            processes.append(pr)

        [pr.join() for pr in processes]
        print(m)

# Виведення:
# Started: Process-2
# Started: Process-3
# Started: Process-5
# Started: Process-4
# Started: Process-6
# Done: Process-3
# Done: Process-5
# Done: Process-2
# Done: Process-6
# Done: Process-4
# {'Process-3': 7444, 'Process-5': 15976, 'Process-2': 15564, 'Process-6': 18896, 'Process-4': 14244}
# У цьому прикладі ми запустили п'ять процесів і додали до словника m, для кожного процесу його pid — ідентифікатор
# процесу. Все це було створено та управлялося менеджером Manager.
