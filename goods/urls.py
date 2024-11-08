from django.urls import path

from goods import views
from goods.views import ProductPageView, CatalogPageView

app_name = 'goods'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:cat_slug>/', CatalogPageView.as_view(), name='catalog'),
    path('product/<slug:product_slug>/', ProductPageView.as_view(), name='product'),
]
