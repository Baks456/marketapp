from django.shortcuts import render

# Create your views here.
from goods.models import Categories, Products


def catalog(request):
    categories = Categories.objects.all().order_by('name').order_by('-sort_level')
    goods = Products.objects.all().order_by('-price')
    context = {
        'title': 'Каталог товаров',
        'categories': categories,
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    context = {
        'title': 'Страница продуктов',
        'content': 'Baks Hi-Tech store'
    }
    return render(request, 'goods/product.html', context)