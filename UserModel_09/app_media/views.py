import os

from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm


def upload_file(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            title = upload_file_form.cleaned_data.get('title')
            description = upload_file_form.cleaned_data.get('description')

            #создали фаил и туда записали все что загрузили с файла
            destination = open('name.txt', 'wb+')
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()

            #Теперь откреом наш файл и счиатем что там записали)
            destination_text = open('name.txt', 'r', encoding='utf=8')
            file_text = destination_text.read()
            destination_text.close()

            bad_text = ['лох', 'сучка', 'дядя']
            #тут сделал каждое слово в массиве отдельно для проверки
            temp_text = file_text.split()
            #тут проверяю по тексту если ли такое слово
            for i_bad in bad_text:
                if i_bad in temp_text:
                    file_text = 'ТУТ ПЛОХОЕ СЛОВО'
                    print(file_text)
            context = [
                'Название', file.name,
                'Описание файла', description,
                'Титл файла', title,
                'Размер', file.size,
                'text :', file_text,

            ]
            return HttpResponse(content=context, status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {
        'form': upload_file_form
    }

    return render(request, 'media/upload_file.html', context=context)