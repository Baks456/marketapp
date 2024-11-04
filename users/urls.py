from django.contrib.auth.views import LogoutView
from django.urls import path

from users import views
from users.views import LoginUser, RegisterUser, UserEditView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('registration', RegisterUser.as_view(), name='registration'),
    path('profile/', UserEditView.as_view(), name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
   path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user-cart/', views.users_cart, name='user_cart'),
]