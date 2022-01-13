from django import forms


class AuthForm(forms.Form):
    mail = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
