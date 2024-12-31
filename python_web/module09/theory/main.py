import requests
from bs4 import BeautifulSoup

BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes(base_url):
    quotes_list = []
    next_page = "/"

    while next_page:
        # Request the page
        response = requests.get(base_url + next_page)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract quotes
        quotes = soup.find_all("div", class_="quote")
        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
            quotes_list.append({"text": text, "author": author, "tags": tags})

        # Check for the next page link
        next_button = soup.find("li", class_="next")
        next_page = next_button.find("a")["href"] if next_button else None

    return quotes_list


def main():
    print("Scraping quotes...")
    quotes = scrape_quotes(BASE_URL)
    for idx, quote in enumerate(quotes[:5], 1):  # Print first 5 quotes for verification
        print(f"Quote {idx}:")
        print(f"  Text: {quote['text']}")
        print(f"  Author: {quote['author']}")
        print(f"  Tags: {', '.join(quote['tags'])}\n")
    print(f"Scraped {len(quotes)} quotes in total.")


if __name__ == "__main__":
    main()
