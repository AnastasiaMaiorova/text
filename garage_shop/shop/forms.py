from typing import Any, Dict
from django import forms
from django.contrib.auth.models import User
from .models import Contact
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Customer


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        print(User.objects.filter(username=username), username)
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError('Пользователь с данным Логином не найден в системе')
        if not user.check_password(password):
            raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    # required=False - не обязательное поле введа
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['address'].label = 'Адрес'
        self.fields['email'].label = 'Почта'
        self.fields['first_name'].label = 'Фамилия'
        self.fields['last_name'].label = 'Имя'

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['net', 'xyz']:
            # 'Регистрация для домена {} невозможна'.format(self.domain)
            raise forms.ValidationError('Регистрация для данного домена невозможна')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Данный почтовый адрес уже зарегистрирован')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        users = User.objects.filter(username=username)
        if len(users) != 0:
            raise forms.ValidationError('Данный логин уже зарегистрирован')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'email', 'last_name', 'first_name', 'phone', 'address',]


class CustomerForm(forms.ModelForm):

    username = forms.CharField(required=True)
    # required=False - не обязательное поле введа
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['address'].label = 'Адрес'
        self.fields['email'].label = 'Почта'
        self.fields['first_name'].label = 'Фамилия'
        self.fields['last_name'].label = 'Имя'

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'phone', 'address',]


# class ContactForm(forms.ModelForm):
#     captcha = ReCaptchaField()
#
#     class Meta:
#         model = Contact
#         fields = ('email', 'captcha')
#         widgets = {
#             'email': forms.TextInput(attrs={'class': 'input'})
#         }
#         labels = {
#             'email': ''
#         }



# НАЧАЛО ВАЖНО
# class LoginForm(forms.ModelForm):
#
#     username = forms.CharField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = Customer
#         fields = ['username', 'password']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].label = 'Логин'
#         self.fields['password'].label = 'Пароль'
#
#     def clean(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         print(Customer.objects.filter(username=username), username)
#         user = Customer.objects.filter(username=username).first()
#         if not user:
#             raise forms.ValidationError('Пользователь с данным Логином не найден в системе')
#         if not user.check_password(password):
#             raise forms.ValidationError('Неверный пароль')
#         return self.cleaned_data
#
#
# class RegistrationForm(forms.ModelForm):
#
#     username = forms.CharField(required=True)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
#     password = forms.CharField(widget=forms.PasswordInput)
#     phone = forms.CharField(required=False)
#     address = forms.CharField(required=False)
#     email = forms.EmailField()
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].label = 'Логин'
#         self.fields['password'].label = 'Пароль'
#         self.fields['confirm_password'].label = 'Подтвердите пароль'
#         self.fields['phone'].label = 'Номер телефона'
#         self.fields['address'].label = 'Адрес'
#         self.fields['email'].label = 'Почта'
#         self.fields['first_name'].label = 'Имя'
#         self.fields['last_name'].label = 'Фамилия'
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         domain = email.split('.')[-1]
#         if domain in ['net', 'xyz']:
#             # 'Регистрация для домена {} невозможна'.format(self.domain)
#             raise forms.ValidationError('Регистрация для данного домена невозможна')
#         if Customer.objects.filter(email=email).exists():
#             raise forms.ValidationError('Данный почтовый адрес уже зарегистрирован')
#         return email
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         users = Customer.objects.filter(username=username)
#         if len(users) != 0:
#             raise forms.ValidationError('Данный логин уже зарегистрирован')
#         return username
#
#     def clean(self):
#         password = self.cleaned_data['password']
#         confirm_password = self.cleaned_data['confirm_password']
#         if password != confirm_password:
#             raise forms.ValidationError('Пароли не совпадают')
#         return self.cleaned_data
#
#     class Meta:
#         model = Customer
#         fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name', 'address', 'phone']
# КОНЕЦ ВАЖНО


# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name', 'address', 'phone']
#
#
# class CustomerEditForm(forms.ModelForm):
#     class Meta:
#         moder = Customer
#         fields = ('email', 'password', 'confirm_password', 'first_name', 'last_name', 'address', 'phone')
