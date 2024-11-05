from django import template

from carts.models import ProductCart

register = template.Library()


@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return ProductCart.objects.filter(user=request.user).select_related('product')
