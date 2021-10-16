from typing import cast
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    title = 'Вести. Главная страница'
    model = Categories.objects.all()
    newses = []
    counter = 0
    for n in reversed(News.objects.all()):
        newses.append(n)
        counter += 1
        if counter == 5:
            break
    return render(request, 'main/index.html', {'title': title, 'model': model, 'newses': newses})


def politic(request):
    title = 'Вести. Политика'
    pol = News.objects.filter(category_id=1)
    model = Categories.objects.all()
    return render(request, 'main/categories/politic.html', {'title': title, 'pol': pol, 'model': model})

def sport(request):
    title = 'Вести. Спорт'
    pol = News.objects.filter(category_id=2)
    model = Categories.objects.all()
    return render(request, 'main/categories/politic.html', {'title': title, 'pol': pol, 'model': model})

def auto(request):
    title = 'Вести. Автомобили'
    pol = News.objects.filter(category_id=4)
    model = Categories.objects.all()
    return render(request, 'main/categories/politic.html', {'title': title, 'pol': pol, 'model': model})

def IT(request):
    title = 'Вести. IT'
    pol = News.objects.filter(category_id=3)
    model = Categories.objects.all()
    return render(request, 'main/categories/politic.html', {'title': title, 'pol': pol, 'model': model})



def medic(request):
    title = 'Вести. Медицина'
    pol = News.objects.filter(category_id=6)
    model = Categories.objects.all()
    return render(request, 'main/categories/politic.html', {'title': title, 'pol': pol, 'model': model})


def else_news(request):
    title = 'Вести. Прочее'
    pol = News.objects.filter(category_id=7)
    model = Categories.objects.all()
    return render(request, 'main/categories/politic.html', {'title': title, 'pol': pol, 'model': model})

def about(request, slug):
    cats = News.objects.filter(pk=slug)
    menu = Categories.objects.all()
    return render(request, 'main/categories/about.html', {'data': cats, 'model': menu})

