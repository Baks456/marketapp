from django import template
from django.db.models import Count, Q
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()


@register.simple_tag()
def show_category():
    s = Categories.objects.annotate(total=Count('products')).filter(Q(slug='all') | Q(total__gt=0)).order_by(
        '-sort_level', 'name')
    return s
    # return Categories.objects.order_by('-sort_level', 'name')


@register.simple_tag(takes_context=True)
def change_param(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
