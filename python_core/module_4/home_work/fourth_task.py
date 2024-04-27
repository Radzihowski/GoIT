def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact updated'

def user_contact(args, contacts):
    name = args[0]
    return contacts[name]

def all_contacts(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command:")
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print("Good bye!")
            break

        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command in ['change', 'update']:
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(user_contact(args, contacts))
        elif command in ['show', 'all', 'print']:
            print(all_contacts(contacts))
        else:
            print('Invalid command.')

if __name__ == '__main__':
    main()