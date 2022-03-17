from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.forms import TextInput, Textarea
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget

from django.contrib.auth.forms import PasswordResetForm




from .models import Comments, Profile


class LoginForm(forms.Form):
    """
    Форма логирования пользователя
    """

    username = forms.CharField(label=False, required=True, widget=forms.TextInput(attrs={
        'class': 'auth-input',
        'placeholder': _('Логин *')
        })
    )

    password = forms.CharField(max_length=50, required=True, label=False, widget=forms.PasswordInput(attrs={
        'placeholder': _("Пароль *"),
        'class': 'auth-input'
    }))


class MyUserRegister(UserCreationForm):
    """
    Форма регистрации пользователя, дополненные поля и условия при создании User
    """

    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': _('Логин')}))

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': _('Email')}) )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'auth-input', 'placeholder': _('Пароль')}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'auth-input', 'placeholder': _('Еще раз пароль')}))


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
        fields = ['username', 'password1', 'password2',  'email']


class EditUserPasswordForm(forms.Form):
    """
    Форма изменения пароля
    """
    old_password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'auth-input', 'placeholder': _('Текущий пароль')}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'auth-input', 'placeholder': _('Пароль')}))
    password2 = forms.CharField(label=False,
        widget=forms.PasswordInput(attrs={'class': 'auth-input', 'placeholder': _('Еще раз пароль')}))

    profile_id = forms.CharField(label=False, required=True, widget=forms.HiddenInput)


    #Проверка что старый пароль совпадает

    # и тогда ошибка валидации будет form.non_field_errors  - ('Пароли не совпали!')
    def clean(self):
        cleaned_data = super(EditUserPasswordForm, self).clean()
        profile = cleaned_data.get('profile_id')
        profile_bd = Profile.objects.get(id=profile)
        old_password = cleaned_data.get('old_password')

        if not profile_bd.user.check_password(old_password):
            raise ValidationError('Старый пароль не совпал')

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('Новые пароли не совпали!')


class EditUserForm(forms.Form):
    """
    Форма редактирования данных пользователя
    """

    GENDER_CHOISE = [
        ('Мужской', _('Мужской')),
        ('Женский', _('Женский'))
    ]

    username = forms.CharField(label=False, max_length=50,
                               widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': _('Логин')}))
    first_name = forms.CharField(label=False, max_length=30, required=False,
                                 widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': _('Имя')}))
    email = forms.EmailField(label=False, required=False,
                             widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': _('Email')}))

    gender = forms.ChoiceField(choices=GENDER_CHOISE, label=_('Выберите пол:'),
                               widget=forms.Select(attrs={'class': 'input_select'}))
    phone = forms.CharField(label=False, required=False,
                            widget=forms.TextInput(
                                attrs={'type': 'tel', 'class': 'auth-input', 'placeholder': _('Телефон:')}))
    avatar = forms.ImageField(required=False, label=_('Новая аватарка:'))

    # birthday = forms.DateTimeField(label=_('Дата рождения'), required=False, widget=forms.DateInput(attrs={'type': 'date'}))


class FullInfoUser(forms.Form):
    """
        Форма дополнительных данных.
        """

    GENDER_CHOISE = [
        ('Мужской', _('Мужской')),
        ('Женский', _('Женский'))
    ]

    first_name = forms.CharField(label=False, max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': _('Имя')}))
    gender = forms.ChoiceField(choices=GENDER_CHOISE, label=_('Выберите пол:'),
                               widget=forms.Select(attrs={'class': 'input_select'}))
    phone = forms.CharField(label=False, required=True,
                            widget=forms.TextInput(
                                attrs={'type': 'tel', 'class': 'auth-input', 'placeholder': _('Телефон:')}))
    avatar = forms.ImageField(required=True, label=_('Выберите аватарку:'))

    # age = forms.IntegerField(label=False, required=True,
    #                          widget=forms.TextInput(
    #                              attrs={'type': 'number', 'class': 'auth-input', 'placeholder': _('Возраст:')}))

    birthday = forms.DateTimeField(label=_('Дата рождения'), required=True, widget=forms.DateInput(attrs={'type': 'date'}))


class BalanceUp(forms.Form):
    """
    Форма пополения баланса личного кабинета
    """

    balance = forms.IntegerField(label=False, required=True, widget=forms.TextInput(attrs={
        'class': 'auth-input ',
        'placeholder': _('Введите сумму пополнения *'),

        })
    )

    def clean_balance(self):
        balance = self.cleaned_data.get('balance')
        if balance <= 0:
            raise ValidationError('Не корректное число')

        return balance


class WriteDreamForm(forms.Form):
    """
    Форма для создания мечты
    """


    title = forms.CharField(label=False, required=True, widget=forms.TextInput(attrs={
        'class': 'input-name',
        'placeholder': _('Название мечты *')
        })
    )

    description = forms.CharField(label=False, required=True, widget=forms.Textarea(attrs={
        'class': 'input-message',
        'placeholder': _('Напишите свою мечту ...'),
        })
    )

    price = forms.IntegerField(label=False, required=True, widget=forms.TextInput(attrs={
        'class': 'upload-sum',
        'placeholder': _('Сумма которая необходима'),
        'type': 'number'
        })
    )

    imgs = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Не корректное число')

        return price

    def clean_title(self):
        title = self.cleaned_data.get('title')
        print(len(title))
        if len(title) > 15:
            raise ValidationError('Какое длинное название -(')
        return title


class EditDreamForm(forms.Form):
    """
    Форма для редактирования созданных мечт
    """
    id_dream = forms.IntegerField()
    push_up = forms.BooleanField(required=False, widget=forms.TextInput(attrs={
        'style': 'display:none',
        })
    )
    cancel = forms.BooleanField(required=False, widget=forms.TextInput(attrs={
        'style': 'display:none',
        })
    )
    active = forms.BooleanField(required=False, widget=forms.TextInput(attrs={
        'style': 'display:none',
        })
    )

    delete = forms.BooleanField(required=False, widget=forms.TextInput(attrs={
        'style': 'display:none',
        })
    )


class RestorePasswordForm(forms.Form):
    """
    Форма восстановления пароля
    """

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': _('Email')}))


    def clean_email(self):
        email = self.cleaned_data['email']
        user_in_bd = User.objects.filter(email=email).first()
        if not user_in_bd:
            raise ValidationError('Такого email нет')
        return email


class CommentForm(forms.ModelForm):
    """
    Форма написания коментария
    """
    # Проверял ckeditor
    # content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Comments
        fields = ['messages']

        # Вот так можно добавлять в нашу форму все что нужно и классы и все такое
        widgets = {
            'messages': Textarea(attrs={
                'placeholder': "Напишите что нибудь!",
            }),



        }


class HelpAmount(forms.Form):
    """
    Форма на получения данных суммы, которую хочет помочь другому пользователю
    """
    amount = forms.IntegerField(label=False, required=True, widget=forms.TextInput(attrs={
        'class': 'upload-sum--help',
        'placeholder': _('Введите сумму помощи *'),
        'data-validate-field': 'price',
        'type': 'number',

         })
    )


    messages_text = forms.CharField(label=False, required=False,
                    widget=forms.Textarea(attrs={
                                'class': 'input-message',
                                'placeholder': _('Напишите текст к своему донату...')
                                })
    )

    my_user_id = forms.CharField(label=False, required=True, widget=forms.HiddenInput)

    #Функия валидации, проверяем что сумму котоырй ввел пользователь, не меньше чем у него есть -)
    def clean(self):
        # Тут метод сразу првоерит это условие и если не будет совпадать будет ошибка) в форме erros _)
        cleaned_data = super(HelpAmount, self).clean()
        amount = cleaned_data.get('amount')
        my_user_id = cleaned_data.get('my_user_id')
        if Profile.objects.filter(user_id=my_user_id).exists():
            user_in_bd = Profile.objects.get(user_id=my_user_id)
            if user_in_bd:
                if user_in_bd.my_balance < amount:
                    raise ValidationError('У Вас на кошельке всего {my_balance} ₽'.format(my_balance=user_in_bd.my_balance))
        else:
            raise ValidationError('Вы не авторизованы!')

class FeedbackForm(forms.Form):
    """
    Форма обратной связи
    """


    name = forms.CharField(label=False, required=True, widget=forms.TextInput(attrs={
        'class': 'input-name name_feedback',
        'placeholder': _('Ваше имя...'),
        'data-validate-field ': 'name',
        })
    )

    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'auth-input email_feedback',
                                 'placeholder': _('Ваш email...'),
                                 'data-validate-field ': 'email',
                                 'type': 'email'
                             })
    )

    text = forms.CharField(label=False, required=True, widget=forms.Textarea(attrs={
        'class': 'input-message messages_feedback',
        'placeholder': _('Текст вашего отзыва...'),
        'data-validate-field ': 'text',
        })
    )


class PopolnenieBoxDream(forms.Form):
    """
      Форма пополнения BOX DREAM
      """

    amount_box = forms.IntegerField(label=False, required=True,
                                widget=forms.TextInput(attrs={
                                        'class': 'upload-sum--help',
                                        'placeholder': _('Введите сумму помощи *'),
                                        'data-validate-field': 'price_box',
                                        'type': 'number',

                                }),
    )

    max_balance_user = forms.IntegerField(label=False, required=True, widget=forms.HiddenInput)

    def clean_amount_box(self):
        amount_box = self.cleaned_data.get('amount_box')
        if amount_box <= 0:
            raise ValidationError('только не 0')

        return amount_box


class CustomPasswordResetForm(PasswordResetForm):
    """
       Форма восстановления пароля
       """

    email = forms.EmailField(label=False, required=True,
                             widget=forms.TextInput(attrs={'class': 'auth-input', 'placeholder': _('Email')}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user_in_bd = User.objects.filter(email=email).first()
        if not user_in_bd:
            raise ValidationError('Такого email нет')
        return email


class CustomePasswordResetConfirmForm(SetPasswordForm):
    """
    Изменения пароля из стандартного чуток под себя переделал -)
    """

    new_password1 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={'class': 'auth-input', 'placeholder': _('Пароль')}))
    new_password2 = forms.CharField(label=False,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'auth-input', 'placeholder': _('Еще раз пароль')}))


class FilterForm(forms.Form):

    FILTER_CHOISE = (
        ('1', _('По дате сначала новые')),
        ('2', _('По дате сначала старые')),
        ('3', _('По собранной сумме по возрастанию')),
        ('4', _('По собранной сумме по убыванию')),
        ('5', _('По желаемой сумме по возрастанию')),
        ('6', _('По желаемой сумме по убыванию')),

    )

    filter_atr = forms.ChoiceField(label=False, required=False, choices=FILTER_CHOISE)