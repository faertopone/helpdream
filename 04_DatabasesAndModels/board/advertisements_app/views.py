from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Advertisement


def advertisement_index(request, *args, **kwargs):
    index = Advertisement.objects.all()
    return render(request, 'advertisements/index.html', {
        'index': index
    })




class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]