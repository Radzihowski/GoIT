# Створення копій об'єктів Python
# Інетпретатор Python ледачий і якщо його явно не попросити створити копію об'єкта, він створить новий вказувник на той
# самий об'єкт. Не завжди така поведінка вітається. Для того, щоб створити копію об'єкта в пакеті copy є функції:
#
# copy -- поверхнева копія
# deepcopy -- глибока копія.
# copy:
#
# Копіює сам об'єкт, але не рекурсивно його внутрішні структури даних. Якщо об'єкт містить посилання на інші об'єкти
# (наприклад, список, словник або інший об'єкт), copy використовує тільки посилання на них, а не створює нові об'єкти.
#
# deepcopy:
#
# Копіює об'єкт, але рекурсивно копіює всі його внутрішні об'єкти. Якщо об'єкт містить внутрішні об'єкти (наприклад,
# вкладені списки, словники тощо), deepcopy створює нові копії цих внутрішніх об'єктів.
from copy import copy, deepcopy

original_list = [1, [2, 3], [4, 5]]

test_list = original_list
test_list.append(3)
print(test_list is original_list)
# Using copy
shallow_copy_list = copy(original_list)
shallow_copy_list.append(3)
shallow_copy_list[1][0] = 'X'
print(original_list)
print(shallow_copy_list)

print(shallow_copy_list == original_list)
# Using deepcopy
deepcopy_list = deepcopy(original_list)
deepcopy_list[1][0] = 'Y'
print(original_list)
print(deepcopy_list)