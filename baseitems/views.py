from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Домашняя страница',
        'content': 'куча текста, который мы придумали'
    }
    return render(request, 'baseitem/index.html', context)

def about(request):
    return HttpResponse("Сайт дорабатываем")

