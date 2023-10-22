# У нас є список показників студентів групи – це список з отриманими балами з тестування. Необхідно поділити список на
# дві частини. Напишіть функцію split_list, яка приймає список (цілі числа), знаходить середнє значення бала у списку
# та ділить його на два списки. У перший потрапляють значення менше середнього, включаючи середнє значення, тоді як у
# другий — строго більше від середнього. Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два
# порожні списки.

def split_list(grade):
    below_average = []
    above_average = []
    sum = 0
    if len(grade) == 0:
        return (below_average, above_average)
    for i in grade:
        sum += i
    average = sum/len(grade)

    for i in grade:
        if i <= average:
            below_average.append(i)
        else:
            above_average.append(i)
    return (below_average, above_average)

print(split_list([1, 2, 3, 4, 62, 43]))
