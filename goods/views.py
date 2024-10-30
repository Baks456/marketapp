from django.shortcuts import render

# Create your views here.
from goods.models import Products


def catalog(request):
    goods = Products.objects.all().order_by('-price')
    context = {
        'title': 'Каталог товаров',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    good = Products.objects.get(slug=product_slug)
    context = {
        'good': good,
    }
    return render(request, 'goods/product.html', context)
