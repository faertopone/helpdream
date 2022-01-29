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

    password = forms.CharField(max_length=50, required=True, label=False, widget=forms.PasswordInput(attrs={
        'placeholder': _("Пароль"),
        'class': 'login__input-form'
    }))


class MyUserRegister(UserCreationForm):

    GENDER_CHOISE = [
        ('Мужской', _('Мужской')),
        ('Женский', _('Женский'))
    ]

    username = forms.CharField(max_length=50, label=_('Логин:'), widget=forms.TextInput(attrs={'class': 'login__input-form', 'placeholder':_('Логин')}))
    first_name = forms.CharField(max_length=30, required=False, label=_('Имя'), widget=forms.TextInput(attrs={'class': 'login__input-form', 'placeholder': _('Имя')}))
    email = forms.EmailField(required=False, label=_('Ваш mail'), widget=forms.TextInput(attrs={'class': 'login__input-form', 'placeholder': _('Email')}) )
    password1 = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput(attrs={'class': 'login__input-form', 'placeholder': _('Пароль')}))
    password2 = forms.CharField(label=_('Повторите пароль'), widget=forms.PasswordInput(attrs={'class': 'login__input-form', 'placeholder': _('Еще раз пароль')}))
    gender = forms.ChoiceField(choices=GENDER_CHOISE, widget=forms.Select(attrs={'class': 'input_select'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'type': 'tel', 'class': 'login__input-form'}))
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
        fields = ['username', 'password1', 'password2', 'first_name', 'email', 'gender', 'phone', 'avatar']


