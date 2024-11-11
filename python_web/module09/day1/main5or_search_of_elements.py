import requests
from bs4 import BeautifulSoup


url = "http://quotes.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
# знайти перший тег <p> на сторінці
first_paragraph = soup.find("p")
print(first_paragraph)

# знайти всі теги <p> на сторінці
all_paragraphs = soup.find_all("p")
print(all_paragraphs)

# отримати текст першого тега <p> на сторінці
first_paragraph_text = first_paragraph.get_text()
print(first_paragraph_text.strip())

# отримати значення атрибута "href" першого тегу <a> на сторінці
first_link = soup.find("a")
first_link_href = first_link["href"]
print(first_link_href)