# Сутності не повинні залежати від інтерфейсів, які вони не використовують.
#
# Коли принцип порушується, модулі схильні до всіх змін в інтерфейсах, від яких вони залежать. Це призводить до високої
# зв'язаності модулів один з одним.
#
# ISP допомагає проектувати інтерфейси так, щоб зміни зачіпали тільки ті модулі, на функціональність яких вони справді
# впливають. Найчастіше це змушує інтерфейси дробити (розділяти).
#
# Припустимо, що у нас є клас Programmer, який описує програміста з офісу деякої компанії. Співробітники пишуть код та
# іноді їдять піцу, яку компанія замовляє в офіс.

class Programmer:
    def write_code(self):
        pass

    def eat_pizza(self, slice_count):
        pass

class OfficeProgrammer(Programmer):
    def __init__(self, name):
        self.name = name

    def eat_pizza(self, slice_count):
        print(f'{self.name} eat {slice_count} slice pizza!')

    def write_code(self):
        print(f'{self.name} write code!')

# Через деякий час компанія почала наймати фрілансерів, які працюють віддалено і піцу не їдять. Якщо ми використовуємо той
# самий інтерфейс, то клас RemoteProgrammer повинен буде реалізувати метод eat_pizza, хоча він йому і не потрібен.

class RemoteProgrammer(Programmer):
    def __init__(self, name):
        self.name = name

    def write_code(self):
        print(f'{self.name} write code!')

    def eat_pizza(self, slice_count):
        pass

# Ми можемо уникнути проблеми з прикладу вище, якщо розділимо клас Programmer. Ми можемо поділити його на дві ролі: CodeProducer
# та PizzaConsumer
class CodeProducer:
    def write_code(self):
        pass
class PizzaConsumer:
    def eat_pizza(self, slice_count):
        pass

class OfficeProgrammer(CodeProducer, PizzaConsumer):
    def __init__(self, name):
        self.name = name

    def eat_pizza(self, slice_count):
        print(f'{self.name} eat {slice_count} slice pizza!')

    def write_code(self):
        print(f'{self.name} write code!')

class RemoteProgrammer(CodeProducer):
    def __init__(self, name):
        self.name = name

    def write_code(self):
        print(f'{self.name} write code!')