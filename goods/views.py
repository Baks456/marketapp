from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from goods.models import Products


def catalog(request, cat_slug):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order = request.GET.get('order', None)

    if cat_slug == 'all':
        goods = Products.objects.order_by('-price')
    else:
        goods = Products.objects.filter(category__slug=cat_slug)
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order and order != 'default':
        goods = goods.order_by(order)

    paginator = Paginator(goods, 6)
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
