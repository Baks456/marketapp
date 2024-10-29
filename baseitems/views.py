from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Baks Hi-Tech store'
    }
    return render(request, 'baseitem/index.html', context)

def about(request):
    context = {
        'title': 'Страница о сайте',
        'content': 'Данный сайт создан потому, что был создан.',
        'text_on_page': 'куча странного текста',
    }
    return render(request, 'baseitem/about.html', context)

