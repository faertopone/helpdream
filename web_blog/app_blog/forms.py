from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from django.forms import TextInput, Textarea, PasswordInput, Select

from .models import Blog, Profile, BlogPhoto
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


class AuthForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
                'placeholder': "логин",
                'class': 'input'
            }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
                'placeholder': "Пароль",
                'class': 'input'
            }))


#ФОРМА ВОССТАНОВЛЕНИЯ ПАРОЛЯ
class RestorePasswordForm(forms.Form):
    # username = forms.CharField(required=True, widget=forms.TextInput(attrs={
    #     'placeholder': "логин",
    #     'class': 'input'
    # }))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': "email",
        'class': 'input'
    }))

    #Это будет в form.non_field_errors
    def clean(self):
        # Тут метод сразу проверит это условие и если не будет совпадать будет ошибка) в форме erros _)
        cleaned_data = super(RestorePasswordForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        email_user_in_bd = User.objects.filter(email=email).first()
        if not email_user_in_bd:
            raise ValidationError('Такой почты нет в  БД')

    # #Это будет в form.username.errors
    # #Проверим что такой пользователь есть
    # def clean_username(self):
    #     data = self.cleaned_data['username']
    #     user_in_bd = User.objects.filter(username=data).first()
    #     if not user_in_bd:
    #         raise ValidationError('Такого пользователя нет')
    #     return data





class MyUserRegister(UserCreationForm):

    STATUS_CHOISE = [
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский')
    ]

    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=30, required=False, label='Имя', help_text='(Не обезательно)')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия', help_text='(Не обезательно)')
    email = forms.EmailField(required=False, label='Ваш mail', help_text='(не обезательно)')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль', )
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль', )
    gender = forms.ChoiceField(choices=STATUS_CHOISE, required=True, widget=forms.Select(attrs={'class': 'input_select'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'type': 'tel'}))
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
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'gender', 'phone', 'avatar']




class BlogPhotoForm(forms.ModelForm):
    multi_img = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = BlogPhoto
        fields = ['multi_img']

class BlogForm(forms.ModelForm):
    author = forms.CharField(required=False)

    class Meta:
        model = Blog
        fields = ['title', 'description']

        #Вот так можно добавлять в нашу форму все что нужно и классы и все такое
        widgets = {
            'description': Textarea(attrs={
                'placeholder': "Описание",
                'class': 'input_description'
            }),
            'title': TextInput(attrs={
                'placeholder': "Заголовок",
                'class': 'input_title',
            })

        }

class EditFormUser(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше новое имя')
    last_name = forms.CharField(max_length=100, label='Ваша новая фамилия')



class UploadFileCsv(forms.Form):
    file_csv = forms.FileField(required=False, label='Загрузить фаил cvs для блогов')



