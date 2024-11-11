from django.urls import path
from django.views.decorators.cache import cache_page

from baseitems.views import IndexPageView, AboutPageView

app_name = 'baseitems'
urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('about/', cache_page(30)(AboutPageView.as_view()), name='about'),

]
