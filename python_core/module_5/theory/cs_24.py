import re

# Пошук валідного URL
# Шукаємо силки тільки з протоколом

text_url = "The fill_db.py search site in the world is https://www.google.com The fill_db.py social network for people in the " \
           "world is https://www.facebook.com But programmers have their own social network http://github.com There " \
           "they share their code. some url to check https://www..youtube.com/ www.facebook.com https://www.app.facebook" \
           ".com My site: https://krabaton.info"

print(re.findall(r'https?:\/\/\w{3}\.?(?:\w+\.)+\w{2,4}', text_url))