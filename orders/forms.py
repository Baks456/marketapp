import re

from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    required_delivery = forms.ChoiceField( choices=[('0', False), ('1', True)], initial='0')
    delivery_address = forms.CharField(required=False)
    payment_on_delivery = forms.ChoiceField( choices=[('0', False), ('1', True)], initial='0')

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if not data.isdigit():
            raise forms.ValidationError('В номере должны быть только цифры')
        patter = re.compile(r'^\d{10}$')
        if not patter.match(data):
            raise forms.ValidationError('В номере должны быть 10 цифр')
        return data


    # first_name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}))
    #
    # last_name = forms.CharField(label='Фамилия', max_length=100, widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}))
    #
    # phone_number = forms.CharField(label='Phone Number', max_length=20, widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}))
    #
    # required_delivery = forms.ChoiceField(label='Required Delivery', required=False,
    #                                       widget=forms.RadioSelect(attrs={'class': 'form-control'}),
    #                                       choices=[('0', False), ('1', True)], initial='0')
    #
    # delivery_address = forms.Textarea(label='Адресс доставки', required=True, widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Введите адресс доставки', 'id': 'delivery-address'}))
    #
    # payment_on_delivery = forms.ChoiceField(label='Payment on Delivery', required=True,
    #                                         widget=forms.RadioSelect(attrs={'class': 'form-control'}),
    #                                         choices=[('0', False), ('1', True)], initial='0')
