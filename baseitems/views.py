from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from goods.models import Categories

def index(request):
    categories = Categories.objects.all().order_by('-sort_level', 'name')
    context = {
        'title': 'Главная страница',
        'content': 'Baks Hi-Tech store',
        'categories': categories,
    }
    return render(request, 'baseitem/index.html', context)

def about(request):
    categories = Categories.objects.all().order_by('-sort_level', 'name')
    context = {
        'title': 'Страница о сайте',
        'content': 'Данный сайт создан потому, что был создан.',
        'text_on_page': 'куча странного текста',
        'categories': categories,
    }
    return render(request, 'baseitem/about.html', context)

