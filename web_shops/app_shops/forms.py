from django import forms

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, User
from django.forms import TextInput, Textarea, PasswordInput, Select


from django.core.exceptions import NON_FIELD_ERRORS, ValidationError



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label=False, required=True, widget=forms.TextInput(attrs={
        'class': 'login__input-form',
        'placeholder': _('Логин')
        })
    )

    password = forms.CharField(required=True, label=False, widget=forms.PasswordInput(attrs={
        'placeholder': _("Пароль"),
        'class': 'login__input-form'
    }))