from django.urls import path

from baseitems import views


app_name = 'baseitems'
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),

]
