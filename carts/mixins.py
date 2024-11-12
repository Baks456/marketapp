from django.template.loader import render_to_string
from django.urls import reverse

from carts.utils import *


class CartsMixin():
    def get_cart(self, request, product=None, cart_id=None):

        if request.user.is_authenticated:
            query_kwargs = {'user': request.user}
        else:
            query_kwargs = {'session_key': request.session.session_key}

        if product:
            query_kwargs['product'] = product

        if cart_id:
            query_kwargs['id'] = cart_id

        return UserCart.objects.filter(**query_kwargs).first()

    def render_cart_details(self, request):
        user_carts = get_user_carts(request)
        context = {'carts': user_carts}

        referer = request.META.get('HTTP_REFERER')
        if reverse('orders:create_order') in referer:
            context['order'] = True

        return render_to_string('carts/includes/include_carts.html', context, request)
