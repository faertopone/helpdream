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


class MyNewsForm(forms.Form):
    titlenews = forms.CharField()
    description = forms.CharField()
    is_active_news = forms.BooleanField(required=False)




class CommentsForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()


class LogginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
