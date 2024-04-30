# Паттерн проектування, який визначає загальний інтерфейс для створення об'єктів в суперкласі, дозволяючи підкласам
# змінювати тип об'єктів, що створюються.
#
# Ви зробили для вашої компанії маркетингову SMS розсилку для споживачів. У якийсь момент компанія замовила мобільний
# застосунок, щоб представляти свій продукт. І виникла необхідність реалізувати маркетингові push розсилки для користувачів.
# Звучить чудово, але ось невдача, більшість вашого коду жорстко зав'язана на смс розсилці. І додавання push розсилок
# торкнеться більшої частини написаного вами коду. А поява email, telegram тощо розсилок змусить виконувати цю роботу
# знову і знову. Все це призводить до коду, що важко читати, наповненого умовними перевірками.
#
# Рішенням є використання патерну фабричний метод. Він пропонує створювати об'єкти не напряму, а через виклик особливого
# фабричного методу. Щоб ця система працювала, всі об'єкти, що повертаються, повинні мати спільний інтерфейс. Підкласи
# зможуть виробляти об'єкти різних класів, що відповідають одному й тому самому інтерфейсу. Найкраще це зрозуміти,
# розглянувши конкретний приклад.
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def create(self):
        pass

    def send_message(self)-> str:
        product = self.create()
        result = product.sending()
        return result

class SendingMessages(ABC):
    @abstractmethod
    def sending(self) -> str:
        pass

class CreatorPush(Creator):
    def create(self) -> SendingMessages:
        return SendingPushMessages()

class CreatorSMS(Creator):
    def create(self) -> SendingMessages:
        return SendingSMSMessages()

class SendingPushMessages(SendingMessages):
    def sending(self) -> str:
        return "Push mailing has been completed"

class SendingSMSMessages(SendingMessages):
    def sending(self) -> str:
        return "SMS mailing has been completed"

def client_code(creator: Creator) -> None:
    print("We know nothing about the creator code that works")
    result = creator.send_message()
    print(f"Result: {result}")

if __name__ == "__main__":
    print("The application performs Push mailing lists.")
    client_code(CreatorPush())
    print("\n")

    print("The application performs SMS mailing.")
    client_code(CreatorSMS())

