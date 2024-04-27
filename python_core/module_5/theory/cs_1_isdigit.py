# str.isdigit(): Перевіряє, чи складається строка лише з цифр.

numbers = ["123", "456", "321", "10", "75", "abc", "23c"]

for num in numbers:
    print(num, num.isdigit())