from _csv import reader
from decimal import Decimal
from datetime import datetime, date, time
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.views import View

from .forms import UploadPriceForm, DocumentForm, MultiFileForm
from .models import Item, File


def items_list(request):
    items = Item.objects.all()
    return render(request, 'goods/items_list.html', {'items_list': items})



def update_price(request):
    # Количество товаров, которые обновили
    count_update_items = 0

    # Количество товаров, которые НЕобновили
    count_noupdate_items = 0

    # Количество артикулы товаров, которых не было в базе данных.
    id_no_items = []

    if request.method == "POST":
        upload_file_form = UploadPriceForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split('\n')
            for i_line in price_str:
                item_str = i_line.split(':')
                #Сначлао из всех обьектов ищем по ID
                filter_items = Item.objects.filter(id_item=item_str[0])
                if filter_items:
                    #Тут по этому ID проверяем все что есть
                    for i_price in filter_items:
                        #Если цена такая же как в файле то ниче не делаем, иначе перезаписываем
                        if i_price.price != Decimal(item_str[1]):
                            filter_items.update(price=Decimal(item_str[1]))
                            count_update_items += 1
                else:
                    count_noupdate_items += 1
                    id_no_items.append(item_str[0])


            # это если csv фаил
            # csv_reader = reader(price_str, delimiter=",", quotechar='"')
            # for row in csv_reader:
            #     Item.objects.filter(code=row[0].update(price=Decimal(row[1])))
            # return HttpResponse(content='Цены были успешно обновлены', status=200)
    else:
        upload_file_form = UploadPriceForm()


    return render(request, 'goods/upload_price_file.html', context={
        'form': upload_file_form,
        'count_update_items': count_update_items,
        'count_noupdate_items': count_noupdate_items,
        'id_no_items': id_no_items,

    })



class Model_form_upload(View):

    def get(self, request):
        file_form = DocumentForm()
        multi_file_form = MultiFileForm()
        return render(request, 'goods/file_form_upload.html', context={'file_form': file_form, 'multi_file_form': multi_file_form})

    def post(self, request):
        file_form = DocumentForm(request.POST, request.FILES)
        multi_file_form = MultiFileForm(request.POST, request.FILES)
        dt = datetime.now()
        dt_now = dt.strftime("%d%m%y-%H-%M-%S")

        if multi_file_form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return redirect('/')


        if file_form.is_valid():
            my_file = file_form.cleaned_data['file']
            new_name_file = dt_now + '_' + str(my_file)
            fs = FileSystemStorage()
            fs.save(new_name_file, my_file)
            file_form.save()
            return redirect('/')

        return render(request, 'goods/file_form_upload.html', context={'file_form': file_form, 'multi_file_form': multi_file_form})

