from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from django.core.exceptions import ValidationError
from django.forms import Textarea, PasswordInput
from django.utils.translation import gettext_lazy as _

from .models import Shops


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label=False, required=True, widget=forms.TextInput(attrs={
        'class': 'login__input-form',
        'placeholder': _('Логин')
        })
    )

    password = forms.CharField(max_length=50, required=True, label=False, widget=forms.PasswordInput(attrs={
        'placeholder': _("Пароль"),
        'class': 'login__input-form'
    }))


class MyUserRegister(UserCreationForm):

    GENDER_CHOISE = [
        ('Мужской', _('Мужской')),
        ('Женский', _('Женский'))
    ]

    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    gender = forms.ChoiceField(choices=GENDER_CHOISE, label=_('Выберите пол:'))
    phone = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    # и тогда ошибка валидации будет form.non_field_errors  - ('Пароли не совпали!')
    def clean(self):
        # Тут метод сразу првоерит это условие и если не будет совпадать будет ошибка) в форме erros _)
        cleaned_data = super(MyUserRegister, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('Пароли не совпали!')

    # и тогда ошибка валидации будет form.username.errors  - ('Такой пользователь уже есть')
    def clean_username(self):
        data = self.cleaned_data['username']
        user_in_bd = User.objects.filter(username=data).first()
        if user_in_bd:
            raise ValidationError('Такой пользователь уже есть')
        return data

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'gender', 'phone', 'avatar']
        widgets = {
            'username': Textarea(attrs={
                'placeholder': "Логин",
                'class': 'input'
            }),
            'password1': PasswordInput(attrs={
                'placeholder': _('Пароль '),
                'class': 'input'
            }),
            'password2': PasswordInput(attrs={
                'placeholder': _('Повторите пароль '),
                'class': 'input'
            }),

            'phone': Textarea(attrs={
                'placeholder': "Телефон",
                'class': 'input',
                'type': 'tel'
            }),

        }



class BuyItems(forms.Form):
    id_item = forms.IntegerField()
    count_item = forms.IntegerField()


class EditItemCart(forms.Form):
    count = forms.IntegerField()
    delete = forms.BooleanField()


class BalanceUpdate(forms.Form):
    money = forms.FloatField(widget=forms.TextInput(attrs={'class': 'input-money'}))