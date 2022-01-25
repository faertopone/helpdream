from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from .models import Blog, Profile, BlogPhoto


class AuthForm(forms.Form):
    username = forms.CharField(label='Ваш логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Ваш пароль')



class MyUserRegister(UserCreationForm):

    STATUS_CHOISE = [
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский')
    ]

    username = forms.CharField(max_length=50, error_messages={'required': 'Please enter your name'} )
    first_name = forms.CharField(max_length=30, required=False, label='Имя', help_text='(Не обезательно)')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия', help_text='(Не обезательно)')
    email = forms.EmailField(required=False, label='Ваш mail', help_text='(не обезательно)')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль', )
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль', )
    gender = forms.ChoiceField(choices=STATUS_CHOISE, required=True, label='Выберите пол', help_text='Не обезательно')
    phone = forms.IntegerField(required=False, label='Телефон', help_text='Не обезательно')
    avatar = forms.ImageField(required=False)

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
    title = forms.CharField(max_length=50, label='Заголовок', help_text='Не более 50 символов')

    class Meta:
        model = Blog
        fields = ['title', 'description']

class EditFormUser(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше новое имя')
    last_name = forms.CharField(max_length=100, label='Ваша новая фамилия')


class UploadFileCsv(forms.Form):
    file_csv = forms.FileField(required=False, label='Загрузить фаил cvs для блогов')



