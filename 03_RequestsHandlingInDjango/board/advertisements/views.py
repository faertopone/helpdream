from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

def index(request, *args, **kwargs):
    category_list = dict()
    category_list = {'О компании': '/about',
                     'Контакты': '/сontacts'
                     }

    return render(request, 'advertisements/index.html', {'category_list': category_list})


class About(TemplateView):
    template_name = 'advertisements/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_company'] = 'Бесплатные объявления'
        context['description_company'] = ['Бесплатные объявления в вашем городе!', 'Лучшие девченки']
        return context


class Contacts (TemplateView):
    template_name = 'advertisements/сontacts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts_list'] = {
            'адрес': 'Лалаленд',
            'телефон': '880090060000',
            'эл. почта': 'хххххххх@бабки.ру'
        }
        return context


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