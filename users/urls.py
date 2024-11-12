from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import LoginUser, RegisterUser, UserEditView, UserCartView, UserPasswordChange

app_name = 'users'

urlpatterns = [
    path('registration', RegisterUser.as_view(), name='registration'),
    path('profile/', UserEditView.as_view(), name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-cart/', UserCartView.as_view(), name='user_cart'),
    path('password-change/', UserPasswordChange.as_view(), name='password_change'),
]
