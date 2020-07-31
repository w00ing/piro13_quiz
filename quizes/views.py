import data as data
from django.shortcuts import render


def index(request):
    return render(request, 'quizes/index.html', data)

def detail(request):
    return render(request, 'quizes/detail.html', data)