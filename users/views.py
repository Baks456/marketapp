from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from users.forms import UserLoginForm


# Create your views here.


# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('baseitems:home'))
#     else:
#         form = UserLoginForm
#
#     context = {'title': 'Авторизация',
#                'form': form
#                }
#     return render(request, 'users/login.html', context)


class LoginUser(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    extra_context = {'title': 'Авторизация'}

    # def get_success_url(self):
    #     return reverse_lazy('baseitems:home')


def profile(request):
    context = {
        'title': 'Профиль пользователя',

    }
    return render(request, 'users/profile.html', context)


def registration(request):
    context = {
        'title': 'Регистрация',

    }
    return render(request, 'users/registration.html', context)

# def user_logout(request):
#     auth.logout(request)
