from pprint import pprint

import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.base_url = 'https://quotes.toscrape.com/'
        self.quotes = []
        self.authors = []

    def paginate(self):
        page_counter = 0
        while True:
            page_counter += 1
            response = requests.get(self.base_url + f"page/{page_counter}/")
            soup = BeautifulSoup(response.text, 'lxml')
            quotes_location = soup.find_all('div', class_='quote')
            pprint(len(quotes_location))
            pprint(quotes_location)
            # pprint(type(quotes_location[0]))
            if not quotes_location:
                break
            self.quote_extractor(quotes_location)

    def quote_extractor(self, sub_objects: list):
        for obj in sub_objects:
            # TO DO: Here will be handle quotes
            self.quotes.append(obj)


if __name__ == "__main__":
    scraper = Scraper()
    scraper.paginate()
