print('test\nNew String')
print('testNew string', end='\n\r')
print('hello world')

main_string = input("Введіть строку: ")
substring = input("Введіть підстроку для пошуку: ")
index = main_string.find(substring)
if index != -1:
    print(f"Підстрока знайдена на позиції: {index}")
else:
    print(f"Підстрока не знайдена!")

s = 'Some words'
print(s.find('o'))
s = 'Some words'
print(s.rfind('o'))

string = 'Виключити з цього [рдяка групи] символів [розташовані між] дужками'
start_index = string.find('[')
end_index = string.find(']')