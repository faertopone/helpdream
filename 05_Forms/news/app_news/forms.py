from django import forms
from .models import User



# class UserForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()
#     first_name = forms.CharField()
#     second_name = forms.CharField()
#     email = forms.EmailField()

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

class NewsForm(forms.ModelForm):
    titleNews = forms.CharField()
    description = forms.CharField()


class CommentsForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField()


class LogginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
