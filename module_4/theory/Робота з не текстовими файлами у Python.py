# Поки що ми розглядали тільки роботу з текстовими фалами в кодуванні UTF-8. Це режим роботи з файлами за замовчуванням.
# Якщо ж потрібно працювати не з текстовими файлами, то можна вказати режим відкриття файлів як b, скорочено від bytes.
# У такому режимі ви отримаєте файловий об'єкт для роботи з файлом в режимі байт-рядків.
with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world')

# В цьому прикладі ми відкрили файл raw_data.bin у режимі для запису "сирих" даних, на що вказує значення wb.
# В цьому режимі у файл можна писати тільки байт-рядки або байт-масиви.
#
# У режимі роботи з "сирими" даними можна відкрити та прочитати вміст будь-якого файлу. Замість терміну “сирі” дані,
# можуть також казати двійкові дані або бінарні дані.

# Отже є ще один контейнер, з яким ми раніше не працювали. Це bytes — байтові рядки.

# Байтові рядки в Python є важливим інструментом для роботи з двійковими даними. Вони дозволяють зберігати та обробляти
# байти, які є основними будівельними блоками даних у комп'ютерах.
#
# У пам'яті комп'ютера дані зберігаються як послідовності байтів. Будь-яка інформація - текст, зображення, звук, тощо -
# може бути представлена у вигляді байтів. Відповідно, будь-які дані можна представити у вигляді послідовності байтів.

# Щоб працювати з послідовністю байтів у Python є вбудовані типи даних байт-рядків
# bytes - незмінний тип, що використовують для представлення байтів.
# bytearray - змінний тип, що дозволяє модифікувати байти після їх створення.R
# Застосування байтових даних досить поширене. Наприклад байтові рядки важливі для роботи з мережевими протоколами
# (наприклад, TCP/IP), послідовними портами, telnet та іншими протоколами, де дані передаються як потік байтів.
# За своєю суттю байт-рядки або простіше байти — це звичайні рядки, але для запису одного символу використовується
# суворо один байт. Це відрізняється від звичайних рядків, де символи (особливо в Unicode) можуть займати більше одного байта.
#
# Але що таке байт та біт насправді для комп'ютера? Розглянемо це більше детально.
# Біт (скорочено від "binary digit" або "двійкова цифра") є основною одиницею інформації в обчислювальній техніці та
# цифровій комунікації. Біт може мати одне з двох значень: 0 або 1. Ви можете думати про біт, як про відповідь на просте
# питання: "так/ні" або "вимкнено/увімкнено".
# Байт - це послідовність з 8 бітів, яка є стандартною одиницею вимірювання кількості інформації в комп'ютерах. Один
# байт може представляти 256 різних станів. Від 00000000 до 11111111 у двійковому форматі або від 0 до 255 десятеричному,
# що дозволяє кодувати широкий спектр інформації, наприклад, символи тексту, частини зображень або звуку.
# У комп'ютерах кожен символ у тексті (наприклад, літера або цифра) зазвичай кодується одним байтом. Наприклад, у
# кодуванні ASCII символ 'A' представляється як 01000001. Усі дані на комп'ютері зберігаються у вигляді байтів. Наприклад,
# текстовий файл розміром у 1 кілобайт займає 1024 байти в пам'яті комп'ютера. Коли дані передаються через інтернет мережу,
# вони також розбиваються на байти.
# Звісно не всі програмісти працюють напряму з бітами та байтами, але розуміти це потрібно. Оскільки біти та байти є
# фундаментом всіх цифрових систем. Вони дозволяють комп'ютерам представляти та обробляти всі види інформації, від простих
# документів до складних відео та звуків.
# Для байт-рядків застосовуються ті самі обмеження і правила, що і для звичайних рядків. Наприклад, ви можете
# використовувати методи upper(), startswith(), index(), find() і так далі.
# Індексація працює так само, як і в звичайних рядках:
#
s = b'Hello!'
print(s[1]) # Виведе: 101 (це ASCII-код символу 'e')