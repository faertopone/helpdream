from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from .import models
from .models import Advertisement


def advertisement_index(request, *args, **kwargs):
    index = Advertisement.objects.all()
    return render(request, 'advertisements/index.html', {
        'index': index
    })




class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisements/advertisements_list.html'
    context_object_name = 'advertisements_list'
    queryset = Advertisement.objects.all()[:5]