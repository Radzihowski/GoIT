import requests
from bs4 import BeautifulSoup


url = "http://quotes.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


# Ви можете отримати доступ до сусідніх елементів за допомогою атрибутів next_sibling та previous_sibling.
# Наприклад, щоб отримати наступний сусідній елемент першого тегу <span> з класом "tag-item" на сторінці:
next_sibling = soup.find("span", attrs={"class": "tag-item"}).find_next_sibling("span")
print(next_sibling)

# Щоб отримати попередній сусідній елемент першого тегу <span> з класом "tag-item" на сторінці:
previous_sibling = next_sibling.find_previous_sibling("span")
print(previous_sibling)

# Знайдемо всі теги <p> на сторінці
p = soup.select("p")
print(p)

# Знайдемо всі елементи з класом "text"
text = soup.select(".text")
print(text)

# Знайдемо всі елементи з ідентифікатором "header". Ідентифікатор - це спеціальний атрибут тегу id.
header = soup.select("#header")
print(header)

# Комбіновані селектори
# Комбіновані селектори шукають елементи, що відповідають кільком умовам.
# Наприклад, знайдемо всі елементи <a> всередині тегу <div> з класом "container":
a = soup.select("div.container a")
print(a)

# Атрибути
# Можна шукати елементи за значенням атрибутів. Знайдемо всі елементи, у яких атрибут href починається з "https://"
href = soup.select("[href^='http://']")
print(href)

# Знайдемо всі елементи, у яких атрибут class містить слово "text":
ctext = soup.select("[class*='text']")
print(ctext)