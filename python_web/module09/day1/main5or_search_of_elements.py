import requests
from bs4 import BeautifulSoup


url = "http://quotes.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
first_paragraph = soup.find("p")
print(first_paragraph)