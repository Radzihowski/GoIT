from collections import UserDict
class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.value = value

    def is_valid(self, value):
        return True

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __str__(self):
        return str(self.value)

class Phone(Field):
    def is_valid(self, value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)
        return phone

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if not phone:
            raise ValueError
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if not phone:
            raise ValueError
        self.add_phone(new_phone)
        self.remove_phone(old_phone)

    def __str__(self):
        return f"Contact name: {str(self.name)}, phones: {', '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        print("***", self.data.get(name))
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name)

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

book = AddressBook() # Створення нової адресної книги

john_record = Record("John") # Створення запису для John
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record) # Додавання запису John до адресної книги

jane_record = Record("Jane") # Створення та додавання нового запису для Jane
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items(): # Виведення всіх записів у книзі
    print(record)

john = book.find("John") # Знаходження та редагування телефону для John
print(john)
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

found_phone = john.find_phone("5555555555") # Пошук конкретного телефону у записі John
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

book.delete("Jane") # Видалення запису Jane