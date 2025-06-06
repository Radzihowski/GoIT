from cli import *
from datetime import datetime, timedelta
import pickle
from colorama import Fore
from utils import py_logger


logger = py_logger.get_logger(__file__)


def load_data(filename="data/addressbook.pkl"):  # Load existing or create a new Address Book
    logger.debug("start load data")
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # return new book if file not found


def save_data(book, filename="data/addressbook.pkl"):  # save Address Book
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def input_error(func):  # Decorator function for error handling
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            logger.error(error)
            if func.__name__ == 'create_contact':
                return "Error creating a contact."
            if func.__name__ == 'phone':
                return "No such contact or the contact has no phone."
            if func.__name__ == 'show_all':
                return "There are no contacts in the Address Book."
            if func.__name__ == 'change_contact':
                return "There is no such contact."

            return "Incorrect command or attribute"
        except IndexError:
            return "Please enter a command with correct argument(s)."
    return inner


@input_error
def parse_input(user_input):  # Parse user input
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def create_contact(name, book: AddressBook):  # Add name to Address Book
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        print("Contact created. ")
    return record


@input_error
def add_phone(args, book: AddressBook):     # Add phone to name record
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
def add_birthday(args, book: AddressBook):  # Add birthday to contact
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
    congrats = f"\n".join(f"Contact: {name}, birthday: {book[name].birthday}, congratulations date: "
                          f"{congrats_day.strftime('%d.%m.%Y')}" for name, congrats_day in congrats_dict_sorted)
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
def hello(args, book: AddressBook):
    return "How can I help you?"


commands = {
    "add [Name] [Number]": "add a name with number to contacts, for example: add Alex 0111222333",
    "add-birthday [Name] [DD.MM.YYYY]": "Add or update the birthday for a contact, for example: "
                                        "add-birthday Alex 21.03.2024",
    "all": "display all records in contacts",
    "birthdays": "display contacts with birthdays in the next 7 days",
    "close": "exit the program",
    "change [Name] [Old Number] [New Number]": "change the phone number for a contact, for example: "
                                               "change Alex 0111222333 0222333444",
    "exit": "exit the program",
    "hello": "greet the bot",
    "phone [Name]": "display the phone number for a contact, for example: phone Alex",
    "show-birthday [Name]": "display the birthday for a contact, for example: show-birthday Alex"
}

def help(args, book: AddressBook):
    print(f"\n".join(f"{Fore.GREEN} {key:40} {Fore.RESET} {value}" for key, value in commands.items()))


@input_error
def phone(args, book: AddressBook):
    name = args[0].title()
    record = book.find(name)
    if not record.phones:
        raise ValueError
    phone_ = f"Contact name: {record.name}, phone(s): {', '.join(str(p) for p in record.phones)}"
    return phone_


@input_error
def show_birthday(args, book: AddressBook):  # Return birthday for a contact
    name = args[0].title()
    record = book.find(name)
    if record.birthday is None:
        raise ValueError
    birthday = f"Contact name: {record.name}, birthday: {record.birthday}"
    return birthday


@input_error
def show_all(args, book: AddressBook):  # Return all records from Address Book
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
    "help": help,
    "hi": hello,
    "phone": phone,
    "show-birthday": show_birthday,
}


def main():
    logger.info("start of fill_db.py file")
    book = load_data()
    handler = CLIHandler()
    # book = AddressBook()
    handler.output_handler("Welcome to the assistant bot!")
    handler.output_handler(f"For a list of commands type {Fore.GREEN}help{Fore.RESET}")
    while True:
        user_input = handler.input_handler()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            handler.output_handler("Good bye!")
            save_data(book)
            break
        elif command in functions:
            handler.output_handler(functions[command](args, book))
        else:
            handler.output_handler("Invalid command.")


if __name__ == "__main__":
    main()