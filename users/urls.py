from django.contrib.auth.views import LogoutView
from django.urls import path

from users import views
from users.views import LoginUser, RegisterUser

app_name = 'users'

urlpatterns = [
    path('registration', RegisterUser.as_view(), name='registration'),
    path('profile/', views.profile, name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
]