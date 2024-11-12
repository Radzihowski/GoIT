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

# Щоб отримати всі дочірні елементи першого тегу <p> на сторінці, використовуємо атрибут children
body_children = list(first_paragraph.children)
print(body_children)
# ['\n', <a href="/login">Login</a>, '\n']

# знайти перший тег <a> всередині першого тегу <div> на сторінці
first_div = soup.find("div")
first_div_link = first_div.find("a")
print(first_div_link)

# Батьківські елементи
# Щоб отримати батьківський елемент першого тегу <p> на сторінці, ми можемо використовувати властивість parent
first_paragraph_parent = first_paragraph.parent
print(first_paragraph_parent)

# Також можна використовувати методи find_parent і find_parents для пошуку батьківських елементів:
container = soup.find("div", attrs={"class": "quote"}).find_parent("div", class_="col-md-8")
print(container)



