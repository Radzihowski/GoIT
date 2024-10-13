# Jinja — це пакет для рендерингу шаблонів. Він має свою власну мета-мову, за допомогою якої він розуміє, як саме
# потрібно сформувати з шаблону готовий документ. Підтримує передачу Python-об'єктів, цикли, оператори розгалуження if.
from jinja2 import Template

name = "Bill"
age = 28

tm = Template("My name is {{ name }} and I am {{ age }} old")
msg = tm.render(name=name, age=age)

print(msg)