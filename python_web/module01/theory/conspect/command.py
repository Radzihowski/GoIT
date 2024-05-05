# Поведінкові патерни

# Ці патерни вирішують завдання ефективної та безпечної взаємодії між об'єктами програми.

# Команда (Command)

# Паттерн проектування, який перетворює запити на об'єкти, дозволяючи передавати їх як аргументи під час виклику методів,
# ставити запити в чергу, логувати їх, а також підтримувати скасування операцій.
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class CommandCreateXMLOrder(Command):
    def __init__(self, receiver, text: str) -> None:
        self._receiver = receiver
        self._text = text

    def execute(self) -> None:
        self._receiver.createXMLOrder(self._text)

class CommandSendEmail(Command):
    def __init__(self, receiver, html: str) -> None:
        self._receiver = receiver
        self._html = html

    def execute(self) -> None:
        self._receiver.send_email(self._html)

class Receiver:
    def createXMLOrder(self, text: str) -> None:
        print(f"Create XML order: {text} ")

    def send_email(self, text: str) -> None:
        print(f"Send email: {text} ")
class Invoker:
    def __init__(self) -> None:
        self._on_order = None
        self._on_email = None

    def set_on_order(self, command: Command):
        self._on_order = command

    def set_on_email(self, command: Command):
        self._on_email = command

    def generate_general_order(self) -> None:
        self._on_order.execute()
        self._on_email.execute()

def client():
    invoker = Invoker()
    invoker.set_on_order(CommandSendEmail(Receiver(), "Send email"))
    invoker.set_on_email(CommandCreateXMLOrder(Receiver(), "Save report"))
    invoker.generate_general_order()

if __name__ == "__main__":
    client()

# Виведення:
#
# Send email: Send email
# Create XML order: Save report
#
# Відправник клас Invoker зберігає посилання на об'єкти команд, у нашому випадку self._on_order та self._on_email, і
# звертається до них, коли потрібно виконати якусь дію. Він працює з командами лише через їхній спільний інтерфейс.
# Він не знає, яку конкретно команду використовує, оскільки отримує готовий об'єкт команди від клієнта.
#
# Команда — абстрактний клас Command, описує загальний для всіх конкретних команд інтерфейс. Зазвичай, це один метод для
# запуску команди.
#
# Конкретні команди, класи CommandCreateXMLOrder та CommandSendEmail, реалізують різні запити, дотримуючись спільного
# інтерфейсу команд. Майже завжди команда передає виклик одержувачу об'єкту бізнес-логіки, клас Receiver.
#
# Одержувач клас Receiver містить бізнес-логіку програми, це може бути будь-який об'єкт. Зазвичай, команди
# перенаправляють виклики одержувачам. Але іноді, щоб спростити програму, ви можете позбавитися одержувачів,
# перемістивши їх код в класи команд.
#
# Клієнт, у нашому випадку функція client, створює об'єкти конкретних команд, передаючи в них усі необхідні параметри,
# а іноді й посилання на об'єкти одержувачів. Після цього клієнт конфігурує відправників створеними командами.