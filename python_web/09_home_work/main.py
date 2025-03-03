import json
import requests

from bs4 import BeautifulSoup
from pprint import pprint


class Scraper:
    def __init__(self):
        self.base_url = 'https://quotes.toscrape.com'
        self.quotes = []
        self.authors = []
        self.authors_urls = set()

    def paginate(self):
        page_counter = 0
        while True:
            page_counter += 1
            response = requests.get(self.base_url + f"/page/{page_counter}/")  # all html from first page
            soup = BeautifulSoup(response.text, 'lxml')  # adding to the soup and reciving object soup
            quotes_location = soup.find_all('div', class_='quote')  # here we are going to have list with 10 elements
            # pprint(len(quotes_location))
            # pprint(quotes_location)
            # pprint(type(quotes_location[0]))
            if not quotes_location:
                break
            self.quote_extractor(quotes_location)

    def quote_extractor(self, sub_objects: list):
        for obj in sub_objects:
            # TO DO: Here will be handle quotes
            # pprint(obj)
            tags_ = obj.find_all('a', class_='tag')
            # print(tags_)
            tags = [t.text.strip() for t in tags_]
            # pprint('________________')
            # pprint(tags)
            author = obj.find('small', class_='author').text.strip()
            author_url = obj.find('a')["href"]
            self.authors_urls.add(author_url)
            # print(author_url)
            # print(author)
            quote = obj.find('span', class_='text').text.strip()
            # print(quote)
            self.quotes.append({"tags": tags, "author": author, "quote": quote})
            # pprint(self.quotes)

    def autor_extractor(self):
        for url in self.authors_urls:
            response = requests.get(self.base_url + url)  # content each of author page
            soup = BeautifulSoup(response.text, 'lxml')  # adding to the soup and reciving object soup
            fullname = soup.find('h3', class_='author-title').text.strip()
            pprint(fullname)
            # TODO add born_date, born_location, description


    def save_to_json(self, mode: str):
        if mode == "quotes":
            data = self.quotes
        elif mode == 'authors':
            data = self.authors
        else:
            raise ValueError("Invalid mode, should be: authors or quotes")
        with open(f"{mode}.json", "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


# {
#     "fullname": "Steve Martin",
#     "born_date": "August 14, 1945",
#     "born_location": "in Waco, Texas, The United States",
#     "description": "Stephen Glenn \"Steve\" Martin is an American actor, comedian, writer, playwright, producer, musician, and composer. He was raised in Southern California in a Baptist family, where his early influences were working at Disneyland and Knott's Berry Farm and working magic and comedy acts at these and other smaller venues in the area. His ascent to fame picked up when he became a writer for the Smothers Brothers Comedy Hour, and later became a frequent guest on the Tonight Show.In the 1970s, Martin performed his offbeat, absurdist comedy routines before packed houses on national tours. In the 1980s, having branched away from stand-up comedy, he became a successful actor, playwright, and juggler, and eventually earned Emmy, Grammy, and American Comedy awards."
# }

if __name__ == "__main__":
    scraper = Scraper()
    scraper.paginate()
    pprint(scraper.quotes)
    # pprint(len(scraper.quotes)) #just to check if all quotes
    scraper.save_to_json(mode='authors')
    # pprint(scraper.authors_urls)
    scraper.autor_extractor()