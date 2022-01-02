from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from .import models
from .models import Advertisement, Author


def advertisement_index(request, *args, **kwargs):
    index = Advertisement.objects.all()
    allAuthor = Author.objects.all()
    return render(request, 'advertisements/news_list.html', {
        'index': index,
        'allAuthor': allAuthor,
    })


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisements/advertisements_list.html'
    context_object_name = 'advertisements_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisements/advertisements_detail.html'
    context_object_name = 'detail_items'