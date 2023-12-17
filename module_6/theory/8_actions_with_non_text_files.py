# Поки що ми розглядали тільки роботу з текстовими фалами в кодуванні UTF-8. Це режим роботи за замовчуванням.
# Якщо ж потрібно працювати не з текстовими файлами, то можна вказати режим відкриття файлів з b, скорочено від bytes.
# У такому режимі ви отримаєте файловий дескриптор для роботи з файлом в режимі байт-рядків.
#
# with open('raw_data.bin', 'wb') as fh:
#     fh.write(b'Hello world!')

# В цьому прикладі ми відкрили файл raw_data.bin у режимі для запису "сирих" даних, на що вказує значення wb.
# В цьому режимі можна писати у файл тільки байт-рядки або байт-масиви.
#
# У режимі роботи з "сирими" даними можна відкрити та прочитати вміст будь-якого файлу, в тому числі й архіву.
