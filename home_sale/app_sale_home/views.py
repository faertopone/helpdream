from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import News, Housing, TypeHousing, NumberRooms

class Index_Main(View):

    def get(self, request):
        news_list = News.objects.all()

        return render(request, 'index.html', {'news_list': news_list})


class SaleHousListView(View):

    def get(self, request):
        hous_list = Housing.objects.all()

        return render(request, 'sale_hous_list.html', {'hous_list': hous_list})

class ContactsView(View):

    def get(self, request):
        return render(request, 'contacts.html', {})

class AboutView(View):

    def get(self, request):
        return render(request, 'about.html', {})


class NewsDetailView(DetailView):
    model = News
    template_name = 'news-detail.html'
    template_name_field = 'news'