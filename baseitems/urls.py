from django.urls import path

from baseitems.views import IndexPageView, AboutPageView

app_name = 'baseitems'
urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

]
