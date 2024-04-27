url = "https://rozetka.com.ua/mobile-phones/c80003/producer=apple;series=iphone-15-pro/#search_text=iphone+15+pro"
url_query = "producer=apple;series=iphone-15-pro/#search_text=iphone+15+pro"
query = url_query.split(';')
print(query)
ob_query = {}
for element in query:
    key, value = element.split('=')
    ob_query.update({key: value})
print(ob_query)

result = []
for key in ob_query:
    result.append(key + '=' + ob_query[key])

print(';'.join(result))