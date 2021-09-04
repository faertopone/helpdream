from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisements_list.html', {})
