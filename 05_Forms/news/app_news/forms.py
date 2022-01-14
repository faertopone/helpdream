from django import forms
from .models import My_User, MyNews, MyComments
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _




class StandartUser(forms.ModelForm):

    username = forms.CharField(label='Введите Ваше имя')
    email = forms.EmailField(label='Введите Ваш mail')
    password1 = forms.CharField(label='Введите Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите Пароль', widget=forms.PasswordInput)

    def clean(self):
        # Тут метод сразу првоерит это условие и если не будет совпадать будет ошибка) в форме erros _)
        cleaned_data = super(StandartUser, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('Повторите пароль еще раз(возможно вы опечатались)')

    class Meta:
        model = User
        fields = ['username', 'email']

        # тут сделали првоерку поля с именем и выведем ошибку свою



class UserForm(forms.ModelForm):

    #тут сделали првоерку поля с именем и выведем ошибку свою
    def clean_username(self):
        data = self.cleaned_data['username']
        if data == 'Сучка':
            raise ValidationError('Нельзя с таким именем')
        return data

    #Тут если надо првоерку сразу 2х полеей, переопределим метод clean
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username == password:
            raise ValidationError('Нельзя что бы пароль и имя были одинаковые!')

    class Meta:
        model = My_User
        fields = '__all__'
        is_active_user = forms.BooleanField(required=False)




class MyNewsForm(forms.ModelForm):

    class Meta:
        model = MyNews
        fields = ['titlenews', 'description', 'is_active_news']
        is_active_news = forms.BooleanField(required=False)






class CommentsForm(forms.ModelForm):

    class Meta:
        model = MyComments
        fields = ['name', 'description']


class LogginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
