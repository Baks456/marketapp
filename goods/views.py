from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from goods.models import Products


def catalog(request, cat_slug, page=1):
    if cat_slug == 'all':
        goods = get_list_or_404( Products.objects.order_by('-price'))
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=cat_slug))

    paginator = Paginator(goods, 3)
    curr_page = paginator.page(page)
    context = {
        'title': 'Каталог товаров',
        'goods': curr_page,
        'cat_slug': cat_slug,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    good = Products.objects.get(slug=product_slug)
    context = {
        'good': good,
    }
    return render(request, 'goods/product.html', context)
