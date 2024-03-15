from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'Главная - Home',
        'content': "Магазин мебели Home"
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title':'Главная - Home',
        'content': "О нас",
        'text_on_page':"Текст о том почему етот магазин такой класний ,и такой ороший товар."
    }
    return render(request, 'main/about.html', context)

