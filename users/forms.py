from captcha.fields import CaptchaField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Введите ваше имя пользователя или Email"}), label='Имя пользователя', required=True)
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль', required=True)
    # captcha = CaptchaField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    # username = forms.CharField()
    # password1 = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Данная почта уже зарегистрирована')
        return email

