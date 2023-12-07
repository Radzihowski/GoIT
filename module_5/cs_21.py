# Регулярний вираз правильний. Можна перевірити regex101 Проблема як шукає сама функція findall.
# Рішенням може бути загорнути весь вираз у групу

text = "Ima.Fool@iana.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.net "

print(re.findall(r'([\w.]+@(\w+\.)+\w{2,})', text))