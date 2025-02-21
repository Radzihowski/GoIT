from pprint import pprint
import sys
from models import Authors, Quotes

class App:
    def __init__(self):
        self.commands = {"name": self.search_by_name,
                         "tag": self.search_by_tag,
                         "tags": self.search_by_tags,
                         "exit": self.exit,
                         }

    def search_by_name(self, value:str):
        # pprint("Start search by name function")
        author = Authors.objects(fullname=value).first()
        # pprint(author)
        if author:
            quotes = Quotes.objects(author=author).all()
            # pprint(quotes)
            return [q.quote for q in quotes]
        return "There are no results with such parameter"

    def search_by_tag(self, tag:str):
        # pprint("Start search by tag function")
        quotes = Quotes.objects(tags__in=[tag])

        if quotes:
            return [q.quote for q in quotes]
        return "There are no results with such parameter"

    def search_by_tags(self, tags:str):
        # pprint("Start search by tags function")
        tags = tags.split(",")
        tags = [t.strip() for t in tags]
        # pprint(tags)
        quotes = Quotes.objects(tags__in=tags)
        if quotes:
            return [q.quote for q in quotes]
        return "There are no results with such parameter"

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
            if not value.strip():
                pprint("Parameter unknown. please use parameter in the next format команда: значення")
                continue
            print(command, value)
            command:str = command.strip()
            if command not in self.commands:
                print("Invalid command")
                continue
            result = self.commands[command](value.strip())
            pprint(result)


if __name__ == "__main__":
    app = App()
    app.run()
