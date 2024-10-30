from goods.models import Categories
from django import template

register = template.Library()

@register.simple_tag()
def show_category():
    return Categories.objects.order_by('-sort_level', 'name')