# Адаптер
#
# Патерн проектування, що дозволяє об'єктам з несумісними інтерфейсами працювати разом. З патерном Адаптер ми вже
# познайомилися, коли розглядали принцип SOLID – Dependency inversion.
#
# У нашому випадку банк надавав інформацію у форматі JSON виду:

[
  {
    'ccy': 'EUR',
    'base_ccy': 'UAH',
    'buy': '37.89060',
    'sale': '39.06250'
  },
  {
    'ccy': 'USD',
    'base_ccy': 'UAH',
    'buy': '36.56860',
    'sale': '37.45318'
  }
]

# Наша функція виведення даних pretty_view працює зі словниками наступного вигляду:

{
  'EUR': {
    'buy': 37.8906,
    'sale': 39.0625
  },
  'USD': {
    'buy': 36.5686,
    'sale': 37.45318
  }
}
#
# На допомогу нам приходить функція-адаптер data_adapter, яка і перетворює дані з API в необхідний словник:
import requests

class RequestConnection:
    def __init__(self, request):
        self.request = request

    def get_json_from_url(self, url):
        return self.request.get(url).json()

class ApiClient:
    def __init__(self, fetch: RequestConnection):
        self.fetch = fetch

    def get_data(self, url):
        responce = self.fetch.get_json_from_url(url)
        return responce

def data_adapter(data: dict):
    return [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]

def pretty_view(data):
    pattern = '|{:^10}|{:^10}|{:^10}|'
    print(pattern.format('currency', 'sale', 'buy'))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get('buy')
        sale = el.get(currency).get('sale')
        print(pattern.format(currency, sale, buy))

if __name__ == '__main__':
    api_client = ApiClient(RequestConnection(requests))

    data = api_client.get_data('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    pretty_view(data_adapter(data))

# За підсумком data_adapter – це перекладач, який трансформує інтерфейс або дані одного об'єкта у такий вигляд, щоб він
# став зрозумілим іншому об'єкту.
# | currency |   sale   |   buy    |
# |   EUR    | 42.91845 |  42.28   |
# |   USD    | 39.84064 |   39.2   |

