from django import forms
from .models import User, MyNews




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
    name = forms.CharField()
    description = forms.CharField()


class LogginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
