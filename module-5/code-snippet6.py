# Split, replace

url_search = 'https://www.google.com/search?q=cats+and+dogs&sca_esv=579468707&source=hp&ei=y2NGZavlEKmgkdUPmbWrqAU&iflsig=AO6bgOgAAAAAZUZx28-7b4wcD0Xgv3zRoXkHQw6LtiSC&ved=0ahUKEwjr9vGB1aqCAxUpUKQEHZnaClUQ4dUDCAw&uact=5&oq=cats+and+dogs&gs_lp=Egdnd3Mtd2l6Ig1jYXRzIGFuZCBkb2dzMgsQLhiABBixAxiDATIFEC4YgAQyBRAuGIAEMgUQLhiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAuGIAEMgUQABiABEi3IlCAAVifIHADeACQAQCYAVSgAf0HqgECMTW4AQPIAQD4AQGoAgrCAhAQABgDGI8BGOUCGOoCGIwDwgIQEC4YAxiPARjlAhjqAhiMA8ICERAuGIAEGLEDGIMBGMcBGNEDwgILEAAYgAQYsQMYgwHCAggQABiABBixA8ICCxAuGIoFGLEDGIMBwgIOEC4YgAQYsQMYxwEY0QPCAgsQABiKBRixAxiDAcICCBAuGIAEGLEDwgIREC4YgwEYxwEYsQMY0QMYgATCAg4QABiABBixAxiDARjJA8ICCBAAGIoFGJIDwgILEC4YgAQYsQMY1ALCAggQLhiABBjUAsICCBAAGIAEGMkDwgIGEAAYFhgewgITEC4YDRiABBixAxiDARixAxiDAcICBxAuGA0YgATCAgcQABgNGIAE&sclient=gws-wiz'
_, query = url_search.split('?')
print(query)
obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value})
print(obj_query)
"""
Методи: split, replace
----
Парсимо query запит для google. Тут класичний роздільник & і перетворюємо на словник із даними
"""
url_search = 'https://www.google.com/search?q=cat+and+dogs&oq=cat+and+dog'
_, query = url_search.split('?')
print(query)
obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)
