from django import forms
from .models import User, MyNews, MyComments
from django.core.exceptions import ValidationError





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
        model = User
        fields = '__all__'
        is_active_user = forms.BooleanField(required=False)
        password = forms.CharField(widget=forms.PasswordInput)



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
