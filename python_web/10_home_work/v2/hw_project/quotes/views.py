from django.shortcuts import render

# Create your views here.
from .utils import get_mongodb


def main(request, page):
    db = get_mongodb()
    quotes = db.quotes.find() # find all quotes
    return render(request, 'quotes/index.html', context={'quotes': quotes} ) #Через контекст прокидуємо квотс в шаблон