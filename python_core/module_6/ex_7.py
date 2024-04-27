# Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source,
# очищений від цифр.
#
# Вимоги:
#
# прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
# запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
# запис нового вмісту файлу output має бути одноразовий і використовувати метод write

def sanitize_file(source, output):
    sanitized_content = ''
    with open(source, 'r') as input_file:
        content = input_file.read()
        for char in content:
            if not char.isdigit():
                sanitized_content += char

        with open(output, 'w') as output_file:
            output_file.write(sanitized_content)


# Solution for my local computer:
def sanitize_file(source, output):
    sanitized_content = ''
    with open(source, 'r') as input_file:
        content = input_file.read()
        for char in content:
            if not char.isdigit():
                sanitized_content += char

        with open(output, 'w') as output_file:
            output_file.write(sanitized_content)


sanitize_file('source', 'output')











