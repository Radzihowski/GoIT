# Тепер завдання — знайти домени першого рівня для електронних адрес, перетворюється на порожню формальність
import re

text = "Ima.Fool@iana.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.net "

print(re.findall(r'@(\w+)\.+(\w{2,})', text))