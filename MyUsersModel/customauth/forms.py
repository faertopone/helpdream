from django import forms


class AuthForm(forms.Form):
    mail = forms.EmailField(label='Введите почтовый адрес')
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
