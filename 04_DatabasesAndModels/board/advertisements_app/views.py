from django.shortcuts import render
from django.views.generic import TemplateView
from advertisements_app.models import Advertisement


def advertisement_index(request, *args, **kwargs):
    index = Advertisement.objects.all()
    return render(request, 'advertisements/index.html', {
        'index': index
    })