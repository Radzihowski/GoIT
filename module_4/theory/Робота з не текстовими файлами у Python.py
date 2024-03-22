# Поки що ми розглядали тільки роботу з текстовими фалами в кодуванні UTF-8. Це режим роботи з файлами за замовчуванням.
# Якщо ж потрібно працювати не з текстовими файлами, то можна вказати режим відкриття файлів як b, скорочено від bytes.
# У такому режимі ви отримаєте файловий об'єкт для роботи з файлом в режимі байт-рядків.
with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world')