from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_1 = [
        'Мастер на час',
        'Выведение из запоя',
        '1231231313123'
    ]
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                      'advertisements_1': advertisements_1})


def about_list(request, *args, **kwargs):
    name_company = ['Бесплатные объявления']
    description_company = ['Бесплатные объявления в вашем городе!', 'Лучшие девченки']

    return render(request, 'advertisements/about.html', {'name_company': name_company,
                                                         'description_company': description_company})




class Region(TemplateView):
        template_name = 'advertisements/regions.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['region_list'] = ['Москва', 'Московская область', 'республика Алтай', 'Вологодская область']
            context['title_region'] = 'Бесплатные регионы'

            return context
  #
  # # Не понял что не атк сделал с ПОСТ? как его вызвать) через form ? но тогда нужно прям сомтреть структуру формы)
  #   def post(self, request):
  #       self.complete_post = ['регион успешно создан']
  #       print('регион успешно создан')
  #       return render(request, 'advertisements/regions.html', {'complete_post': self.complete_post})
  #

# def regions_list(request, *args, **kwargs):
#     region_list = ['Москва', 'Московская область', 'республика Алтай', 'Вологодская область']
#
#     return render(request, 'advertisements/regions.html', {'region_list': region_list})