# Порівняння рядків
# Порівняння рядків у Python може давати неоднозначний результат внаслідок того, що в UTF-8 кодуванні один і той самий
# символ можна представити декількома кодами, наприклад, символ 'ê' можна представити кодом U+00EA, або як послідовність
# двох кодів U+0065 та U+0302. З цієї причини порівняння одного і того самого символу може повернути False через
# відмінності у записі.
# Щоб розв'язати цю проблему при роботі з не ASCII символами для порівняння рядків, їх необхідно нормалізувати за
# допомогою методу casefold, який повертає рядок, де всі символи у нижньому регістрі і без неоднозначностей,
# коли будь-який символ матиме тільки одну можливу форму запису.