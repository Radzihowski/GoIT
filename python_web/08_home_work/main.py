import json
from pprint import pprint
from models import Authors, Quotes
from datetime import date, datetime

def fill_authors():
    with open("authors.json", 'r') as file:
        authors_list = json.load(file)
        for el in authors_list:
            fullname = el["fullname"]
            born_date = el.get("born_date")
            born_date_dt = datetime.strptime(born_date, "%B %d, %Y")
            born_location = el.get("born_location")
            description = el.get("description")
            pprint(fullname)
            pprint(born_date_dt)
            pprint(born_location)
            pprint(description)
            author = Authors(fullname=fullname, born_date=born_date_dt, born_location=born_location,
                             description=description)
            author.save()

def fill_quotes():
    ...

if __name__ == "__main__":
    fill_authors()