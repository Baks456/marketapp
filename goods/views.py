from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

# Create your views here.
from goods.models import Products
from goods.utils import q_search


class ProductPageView(DetailView):
    model = Products
    template_name = 'goods/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'good'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.category.name} - {self.object.name}'
        return context

    def qet_object(self, queryset=None):
        return get_object_or_404(Products, slug=self.kwargs[self.slug_url_kwarg])


class CatalogPageView(ListView):
    model = Products
    template_name = 'goods/catalog.html'
    context_object_name = 'goods'
    paginate_by = 6
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Каталог товаров'
        return context

    def get_queryset(self):
        cat_slug = self.kwargs['cat_slug']
        on_sale = self.request.GET.get('on_sale')
        order = self.request.GET.get('order')

        if cat_slug == 'all' or cat_slug is None:
            goods = Products.objects.order_by('-price')
        else:
            goods = Products.objects.filter(category__slug=cat_slug)

        if on_sale:
            goods = goods.filter(discount__gt=0)
        if order and order != 'default':
            goods = goods.order_by(order)
        return goods


def search(request, cat_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order = request.GET.get('order', None)
    search_field = request.GET.get('q', None)

    if cat_slug == 'all':
        goods = Products.objects.order_by('-price')
    elif search_field:
        goods = q_search(search_field)
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
    return render(request, 'goods/search.html', context)

# def product(request, product_slug):
#     good = Products.objects.get(slug=product_slug)
#     context = {
#         'good': good,
#     }
#     return render(request, 'goods/product.html', context)


# def catalog(request, cat_slug=None):
#     page = request.GET.get('page', 1)
#     on_sale = request.GET.get('on_sale', None)
#     order = request.GET.get('order', None)
#
#     if cat_slug == 'all' or cat_slug is None:
#         goods = Products.objects.order_by('-price')
#     else:
#         goods = Products.objects.filter(category__slug=cat_slug)
#     if on_sale:
#         goods = goods.filter(discount__gt=0)
#     if order and order != 'default':
#         goods = goods.order_by(order)
#
#     paginator = Paginator(goods, 6)
#     curr_page = paginator.page(page)
#     context = {
#         'title': 'Каталог товаров',
#         'goods': curr_page,
#         'cat_slug': cat_slug,
#     }
#     return render(request, 'goods/catalog.html', context)
