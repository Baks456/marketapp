from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, TemplateView

from baseitems.cachemixins import CacheMixin
from carts.models import UserCart
from orders.models import Order, OrderItem
from users.forms import UserLoginForm, RegisterUserForm, UserUpdateForm, UserPasswordChangeForm


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
            # old_carts = UserCart.objects.filter(user=user)
            # if old_carts.exists():
            #     old_carts.delete()
            UserCart.objects.filter(session_key=session_key).update(user=user)
            session_key = None
            return HttpResponseRedirect(self.get_success_url())


class RegisterUser(SuccessMessageMixin, CreateView):
    template_name = 'users/registration.html'
    form_class = RegisterUserForm
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('catalog:catalog', kwargs={'cat_slug': 'all'})
    success_message = 'Аккаунт зарегистрирован'

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            if session_key:
                UserCart.objects.filter(session_key=session_key).update(user=user)

            return HttpResponseRedirect(self.success_url)


@method_decorator(login_required, name="dispatch")
class UserEditView(SuccessMessageMixin, CacheMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = UserUpdateForm
    success_message = 'Данные пользователя успешно изменены'
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мой профиль'

        cache_info = Order.objects.filter(user=self.request.user).prefetch_related(
            Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('product'))).order_by('-id')

        context['orders'] = self.set_or_get_cache(cache_info, f'orders_cache_{self.request.user.id}', 60)
        return context


class UserCartView(TemplateView):
    template_name = 'users/user_cart.html'


class UserPasswordChange(SuccessMessageMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change_form.html'
    success_message = 'Пароль успешно изменен, войдите под новым паролем'
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'Изменение пароля пользователя'}

# @method_decorator(login_required, name="dispatch")
# class UserLogoutView(SuccessMessageMixin, LogoutView):
#     success_message = 'Вы вышли из аккаунта'


# def users_cart(request):
#     return render(request, 'users/user_cart.html')

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
