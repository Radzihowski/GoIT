# Паттерн проектування, який створює механізм підписки, що дозволяє одним об'єктам стежити і реагувати на події, що
# відбуваються в інших об'єктах.
#
# Уявіть, що ви хочете придбати якийсь унікальний товар в інтернет-магазині. Ви щодня заходите на сайт і перевіряєте,
# чи не з'явився товар. Ви витрачаєте час і не щасливі, що товару все немає. Можна підписатися на спам розсилку нових
# товарів у магазині. Але більшість товарів вам зовсім не потрібні, і шукати в розсилці, чи з'явилася потрібна вам річ,
# чи ні — те ще заняття.
#
# Рішення — це паттерн Спостерігач. В інтернет-магазині з'являється кнопка повідомити мене, коли товар з'явиться.
# Ви натискаєте на неї, підписуєтеся на подію, і з появою товару магазин повідомляє вам, що товар з'явився. Фактично
# інтернет-магазин — це видавець, який володіє внутрішнім станом, поява товару якого цікава для підписників (покупців).
# Він містить механізм підписки — список підписників, а також методи підписки/відписки. Коли товар з'являється видавець
# сповіщає своїх підписників. Для цього видавець проходить списком підписників (всіх, хто натиснув кнопку) і викликає
# їх метод повідомлення, заданий в інтерфейсі підписника.
#
# Давайте розглянемо конкретний приклад:
#
from abc import ABC, abstractmethod

class Publisher(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

class PublisherMessages(Publisher):
    _observers = []
    _indicator = 0

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def business_logic_execution(self):
        print(f"Application logic is being executed. Indicator:{self._indicator}")
        self._indicator += 1
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, publisher):
        pass
class ObserverA(Observer):
    def update(self, publisher):
        if publisher._indicator <= 3:
            print("ObserverA: reacts to the indicator less than 2")

class ObserverB(Observer):
    def update(self, publisher):
        if publisher._indicator > 2:
            print("ObserverB: reacts to the indicator more than 2")

def client():
    publisher = PublisherMessages()

    observer_a = ObserverA()
    publisher.attach(observer_a)

    observer_b = ObserverB()
    publisher.attach(observer_b)

    publisher.business_logic_execution()
    print("first execution of business logic")
    publisher.business_logic_execution()
    print("second execution of business logic")
    publisher.detach(observer_a)
    publisher.business_logic_execution()
    print("third execution of business logic")

if __name__ == "__main__":
    client()
# Що відбувається у нас. Ми створюємо екземпляр Видавця
#
# publisher = PublisherMessages()
#
# Після цього ми створюємо екземпляри двох підписників і підписуємо їх на видавця
#

# observer_a = ObserverA()
# publisher.attach(observer_a)
#
# observer_b = ObserverB()
# publisher.attach(observer_b)
#
# Починаємо виконувати метод business_logic_execution з якоюсь бізнес-логікою Видавця.

# publisher.business_logic_execution()
# publisher.business_logic_execution()
# publisher.detach(observer_a)
# publisher.business_logic_execution()
#
# І при кожному виконанні методу business_logic_execution виконується метод self.notify(), який проходить списком
# підписників та виконує у них метод update. Всередину методу update ми передаємо посилання на об'єкт видавця, щоб
# підписник міг стежити за властивістю _indicator та реагувати відповідно.
#
# Все це призводить до наступного виведення:
# Application logic is being executed. Indicator:0
# ObserverA: reacts to the indicator less than 2
# first execution of business logic
# Application logic is being executed. Indicator:1
# ObserverA: reacts to the indicator less than 2
# second execution of business logic
# Application logic is being executed. Indicator:2
# ObserverB: reacts to the indicator more than 2
# third execution of business logic
