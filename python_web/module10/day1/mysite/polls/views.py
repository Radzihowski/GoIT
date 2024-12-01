from django.shortcuts import HttpResponse

# Create your views here.
def index(reques):
    return HttpResponse("Hello, world. You are the polls index.")