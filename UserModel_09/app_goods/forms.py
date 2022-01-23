from django import forms

from .models import File


class UploadPriceForm(forms.Form):

    file = forms.FileField()


class DocumentForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['description', 'file']


class MultiFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)