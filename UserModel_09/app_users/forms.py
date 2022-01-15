from django import forms
from django.contrib.auth.forms import UserCreationForm, User

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class ExtendedREgisterForm(UserCreationForm):

    STATUS_CHOISE = [
        ('Москва', 'Москва'),
        ('Питер', 'Питер')
    ]

    username = forms.CharField(max_length=50, label='Логин', help_text='Не более 50 символов')
    first_name = forms.CharField(max_length=30, required=False, label='Имя', help_text='(Не обезательно)')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия', help_text='(Не обезательно)')
    email = forms.EmailField(required=False, label='Ваш mail', help_text='(не обезательно)')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль', help_text='Придумайте хороший пароль!')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль', help_text='Еще раз введите такой же пароль!')
    date_of_birth = forms.DateTimeField(required=True, label='Дата рождения', help_text='Обезательно к заполнению!')
    # city = forms.ChoiceField(choices=['Москва', 'Питер'], required=False, label='Выберите город', help_text='Не обезательно')
    city = forms.ChoiceField(choices=STATUS_CHOISE, required=False, label='Выберите город', help_text='Не обезательно' )



    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'date_of_birth', 'city']

