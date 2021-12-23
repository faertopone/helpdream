from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

count_get = 0

def index(request, *args, **kwargs):
    category_list = dict()
    category_list = {'О компании': '/about',
                     'Контакты': '/сontacts',
                     'Регионы': '/regions',
                     'Список услуг': 'advertisements'
                     }
    methods = request.META.get('REQUEST_METHOD')
    print(methods)
    succes_post = '-----'
    if methods == 'POST':
        succes_post = 'Метод пост прошел'

    return render(request, 'advertisements/index.html', {'category_list': category_list,
                                                        'succes_post': succes_post
                                                         })


class About(TemplateView):
    template_name = 'advertisements/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['name_company'] = 'Бесплатные объявления'
        context['description_company'] = ['Бесплатные объявления в вашем городе!', 'Лучшие девченки']

        return context


class Advertisements(TemplateView):
    template_name = 'advertisements/advertisements.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisements_list'] = ['Курсы', 'Подробнее об методе ПОСТ', 'Не придумал название', 'И последний пнукт']

        global count_get
        count_get += 1
        context['count'] = str(count_get)

        return context


class Contacts(TemplateView):
    template_name = 'advertisements/сontacts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts_list'] = {'адрес': 'Шлюшандра 123', 'телефон': '9999999999', 'эл. почта': '1хбетсобакару'}

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