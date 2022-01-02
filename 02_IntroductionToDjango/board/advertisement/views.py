from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisements_list.html', {})

def index(request, *args, **kwargs):
    return render(request, 'advertisement/news_list.html', {})

def kurs_1(request, *args, **kwargs):
    return render(request, 'advertisement/kurs_1_list.html', {})
def kurs_2(request, *args, **kwargs):
    return render(request, 'advertisement/kurs_2.html', {})
def kurs_3(request, *args, **kwargs):
    return render(request, 'advertisement/kurs_3.html', {})
def kurs_4(request, *args, **kwargs):
    return render(request, 'advertisement/kurs_4.html', {})
def kurs_5(request, *args, **kwargs):
    return render(request, 'advertisement/kurs_5.html', {})