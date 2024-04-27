from cli import *
from datetime import datetime, timedelta

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == 'create_contact':
                return "Error creating a contact."
            if func.__name__ == 'phone':
                return "No such contact."
            if func.__name__ == 'show_all':
                return "There are no contacts in the Address Book."
            if func.__name__ == 'change_contact':
                return "There is no such contact."

            return "Incorrect command or attribute"
        except IndexError:
           return "Please enter a command with correct argument(s)."
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def create_contact(name, book: AddressBook):
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        print("Contact created. ")
    return record

@input_error
def add_phone(args, book: AddressBook):
    name = args[0].title()
    phone_ = args[1]
    record = book.find(name)
    if record is None:
        record = create_contact(name, book)
    message = "Phone number added."
    if phone_:
        record.add_phone(phone_)
    return message

@input_error
def add_birthday(args, book: AddressBook):
    name = args[0].title()
    birthday = args[1]
    record = book.find(name)
    if record is None:
        record = create_contact(name, book)
    message = "Birthday added/updated."
    if birthday:
        record.add_birthday(birthday)
    return message

@input_error
def birthdays(args, book: AddressBook):
    today = datetime.today().date()
    congrats_dict = {}
    for name, birthday in book.items():
        if birthday.congrats_date() <= today + timedelta(days=7):
            congrats_day = birthday.congrats_date()
            congrats_dict[name] = congrats_day

    congrats_dict_sorted = sorted(congrats_dict.items(), key=lambda x: x[1])

    congrats_header = "\nUpcoming birthdays in the next 7 days:\n"
    congrats = f"\n".join(f"Congratulations date: {congrats_day.strftime('%d.%m.%Y')}, "f"contact: {name}, "
                          f"birthday: {book[name].birthday}" for name, congrats_day in congrats_dict_sorted)
    if not congrats:
        congrats = "No upcoming birthdays\n"
    return congrats_header + congrats

@input_error
def change_contact(args, book: AddressBook):
    name = args[0].title()
    old_phone = args[1]
    new_phone = args[2]
    if not book.find(name):
        raise ValueError
    rec = book.find(name)
    rec.edit_phone(old_phone, new_phone)
    return "Phone number updated."

@input_error
def hello(args, book:AddressBook):
    return "How can I help you?"

@input_error
def phone(args, book: AddressBook):
    name = args[0].title()
    record = book.find(name)
    if record.phones is None:
        raise ValueError
    phone_ = f"Contact name: {record.name}, phone(s): {', '.join(str(p) for p in record.phones)}"
    return phone_

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0].title()
    record = book.find(name)
    if record.birthday is None:
        raise ValueError
    birthday = f"Contact name: {record.name}, birthday: {record.birthday}"
    return birthday

@input_error
def show_all(args, book: AddressBook):
    if not book:
        raise ValueError
    return book

functions = {
    "add": add_phone,
    "add-birthday": add_birthday,
    "all": show_all,
    "birthdays": birthdays,
    "change": change_contact,
    "hello": hello,
    "hi": hello,
    "phone": phone,
    "show-birthday": show_birthday,
}

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in functions:
            print(functions[command](args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()