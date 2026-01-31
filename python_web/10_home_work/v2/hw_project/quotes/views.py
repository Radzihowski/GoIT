from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Author, Quote, Tag
from django.contrib.auth.decorators import login_required

# Create your views here.
from .utils import get_mongodb

def main(request, page=1):
    # db = get_mongodb()
    # quotes = db.quotes.find() # find all quotes
    quotes = Quote.objects.all() # Отримуємо всі квоти з бази даних
    per_page = 10
    paginator = Paginator(list(quotes), per_page) # Це скільки буде на сторінці
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})  # Через контекст прокидуємо квотс в шаблон

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.user = request.user
            new_author.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/authors.html', context={'form': form})
    return render(request, 'quotes/authors.html', context={'form': AuthorForm()})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.save()
            form.save_m2m()
            return redirect(to='quotes:root')
        else:
            return render(request,'quotes/quote.html', context={'form': form})
    return render(request, 'quotes/quote.html', context={'form': QuoteForm()})

@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/tag.html', context={'form': form})
    return render(request, 'quotes/tag.html', context={'form': TagForm()})

def author_about(request, id):
    author = Author.objects.get(pk=id)
    return render(request, 'quotes/author.html', context={'author': author})