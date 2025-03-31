from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find() # find all quotes
    per_page = 10
    paginator = Paginator(list(quotes), per_page) # Це скільки буде на сторінці
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})  # Через контекст прокидуємо квотс в шаблон
