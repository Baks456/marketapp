from django.urls import path

from carts import views
from carts.views import CartAddView, CartChangeView, CartDeleteView

app_name = 'carts'

urlpatterns = [
    path('cart_add/', CartAddView.as_view(), name='cart_add'),
    path('cart_change/', CartChangeView.as_view(), name='cart_change'),
    path('cart_remove/', CartDeleteView.as_view(), name='cart_remove'),
]