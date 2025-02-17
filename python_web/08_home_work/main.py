from pprint import pprint
import sys

class App:
    def __init__(self):
        self.commands = {"name": self.search_by_name,
                         "tag": self.search_by_tag,
                         "tags": self.search_by_tags,
                         "exit": self.exit,
                         }

    def search_by_name(self, value:str):
        pass

    def search_by_tag(self, tag:str):
        pass

    def search_by_tags(self, tags:str):
        ...

    def exit(self, *args):
        pprint("Thank you! Have a nice day!")
        sys.exit(0)
    def run(self):
        while True:
            user_input = input("Enter search query in next format команда: значення >>> ")
            if user_input == "exit":
                self.exit()
            if ":" not in user_input:
                pprint("Command unknown. please use command in the next format команда: значення")
                continue
            command,value,*_ = user_input.split(":")
            print(command, value)
            command:str = command.strip()
            if command not in self.commands:
                print("Invalid command")
                continue
            self.commands[command](value)



if __name__ == "__main__":
    app = App()
    app.run()
