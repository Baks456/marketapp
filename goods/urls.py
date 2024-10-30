from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('<slug:cat_slug>/', views.catalog, name='catalog'),
    path('<slug:cat_slug>/<int:page>/', views.catalog, name='catalog'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
