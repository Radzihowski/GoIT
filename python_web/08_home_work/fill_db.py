import json
from pprint import pprint
from models import Authors, Quotes
from datetime import date, datetime


pprint("execute fill_db.py")

def fill_authors():
    with open("authors.json", 'r', encoding='utf-8') as file:
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
    with open("quotes.json", 'r', encoding='utf-8') as file:
        quotes_list = json.load(file)
        for el in quotes_list:
            tags = el.get("tags")
            author_name = el.get("author")
            quote_text = el.get("quote")
            pprint(tags)
            pprint(author_name)
            pprint(quote_text)
            author = Authors.objects(fullname=author_name).first()
            if not author:
                print(f" Warning: Author '{author_name}' not found if database. Skipping quote. ")
                continue

            quote = Quotes(tags=tags, author=author, quote=quote_text)
            quote.save()


if __name__ == "__main__":
    fill_authors()
    fill_quotes()