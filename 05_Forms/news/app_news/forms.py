from django import forms
from .models import User, MyNews, MyComments




class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


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
    password = forms.CharField()
