import abc
from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.value = value

    def is_valid(self, value):
        return True

    def __str__(self):
        return str(self.value)

class Birthday(Field):
    def is_valid(self, value):
        return bool(datetime.strptime(value, "%d.%m.%Y"))

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __str__(self):
        return str(self.value)

class Phone(Field):
    def is_valid(self, value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, value):
        self.name = Name(value)
        self.phones = []
        self.birthday = None

    def add_birthday(self, value):
        birthday = Birthday(value)
        self.birthday = birthday
        return birthday

    def congrats_date(self):
        today = datetime.today().date()
        birthday = datetime.strptime(str(self.birthday), "%d.%m.%Y").date()

        if datetime(today.year, birthday.month, birthday.day).date() < today:
            next_birthday = (datetime(today.year + 1, birthday.month, birthday.day)).date()
        else:
            next_birthday = datetime(today.year, birthday.month, birthday.day).date()

        if next_birthday.isoweekday() in [6, 7]:
            congrats_date = next_birthday + timedelta(days=(8 - next_birthday.isoweekday()))
        else:
            congrats_date = next_birthday

        return congrats_date

    def add_phone(self, value):
        phone = Phone(value)
        self.phones.append(phone)
        return phone

    def find_phone(self, value):
        for phone in self.phones:
            if phone.value == value:
                return phone

    def remove_phone(self, value):
        phone = self.find_phone(value)
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
        return (f"Contact name: {str(self.name)}, phone(s): {', '.join(str(p) for p in self.phones)}, "
                f"birthday: {str(self.birthday)} ")

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name)

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

class ABCHandler(abc.ABC):
    @abc.abstractmethod
    def input_handler(self):
        ...

    @abc.abstractmethod
    def output_handler(self, data):
        ...

class CLIHandler(ABCHandler):
    def input_handler(self):
        user_input = input("Enter a command: ")
        return user_input

    def output_handler(self, data):
        print(data)

