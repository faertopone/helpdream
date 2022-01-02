from django import forms
from .models import User, MyNews, MyComments




class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class MyNewsForm(forms.ModelForm):
    titlenews = forms.CharField()
    description = forms.CharField()
    is_active_news = forms.BooleanField(required=False)

    class Meta:
        model = MyNews
        fields = '__all__'






class CommentsForm(forms.ModelForm):

    class Meta:
        model = MyComments
        fields = ['name', 'description']


class LogginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
