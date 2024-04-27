print('test\nNew String')
print('testNew string', end='\n\r')
print('hello world')

# main_string = input("Введіть строку: ")
# substring = input("Введіть підстроку для пошуку: ")
# index = main_string.find(substring)
# if index != -1:
#     print(f"Підстрока знайдена на позиції: {index}")
# else:
#     print(f"Підстрока не знайдена!")
#
# s = 'Some words'
# print(s.find('o'))
# s = 'Some words'
# print(s.rfind('o'))
#
# string = 'Виключити з цього [рдяка групи] символів [розташовані між] дужками'
# start_index = string.find('[')
# end_index = string.find(']')
#
# new_string = string[:start_index] + string[end_index + 1]
# print(new_string)


def sanitize(string):
    new_string = string[:]  # копія строки
    while True:
        start_index = new_string.find('[')
        end_index = new_string.find(']')
        if start_index == -1:
            break
        new_string = new_string[:start_index] + new_string[end_index + 1:]
    return new_string

print(sanitize('Виключити з цього [рдяка групи] символів [розташовані між] дужками'))
