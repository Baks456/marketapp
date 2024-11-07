from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Prefetch
from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from carts.models import ProductCart
from orders.models import UserOrder, OrderItem
from users.forms import UserLoginForm, RegisterUserForm, UserUpdateForm


# Create your views here.


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    extra_context = {'title': 'Авторизация'}
    success_message = f' Добро пожаловать!'


    def get_success_url(self):
        redirect_to = self.request.POST.get('next', None)
        if redirect_to and redirect_to != reverse('users:login'):
            return redirect_to
        return reverse_lazy('catalog:catalog', kwargs={'cat_slug': 'all'})

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()
        if user:
            auth.login(self.request, user)
            # old_carts = ProductCart.objects.filter(user=user)
            # if old_carts.exists():
            #     old_carts.delete()
            ProductCart.objects.filter(session_key=session_key).update(user=user)
            session_key = None
            return HttpResponseRedirect(self.get_success_url())




class RegisterUser(CreateView, SuccessMessageMixin):
    template_name = 'users/registration.html'
    form_class = RegisterUserForm
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')
    success_message = 'Аккаунт зарегистрирован'


@method_decorator(login_required, name="dispatch")
class UserEditView(UpdateView, SuccessMessageMixin):
    template_name = 'users/profile.html'
    form_class = UserUpdateForm
    extra_context = {'title': 'Мой профиль'}
    success_message = 'Данные пользователя успешно изменены'


    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мой профиль'
        context['orders'] = UserOrder.objects.filter(user=self.request.user).prefetch_related(Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('product'))).order_by('-id')
        return context

@method_decorator(login_required, name="dispatch")
class UserLogoutView(LogoutView, SuccessMessageMixin):
    success_message = 'Вы вышли из аккаунта'


def users_cart(request):
    return render(request, 'users/user_cart.html')

# def user_logout(request):
#     auth.logout(request)

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

# def registration(request):
#     context = {
#         'title': 'Регистрация',
#
#     }
#     return render(request, 'users/registration.html', context)

# def profile(request):
#     context = {
#         'title': 'Профиль пользователя',
#
#     }
#     return render(request, 'users/profile.html', context)


