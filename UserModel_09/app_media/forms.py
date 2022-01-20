from django import forms



class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, label='Название файла', help_text='подсказкак какая нить')
    description = forms.CharField(max_length=10, label='Краткое описание файла', help_text='подсказкак какая нить')
    file = forms.FileField()