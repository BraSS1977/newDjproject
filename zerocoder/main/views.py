from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request, 'main/index.html')

def new(request):
    return render (request, 'main/new.html')

def Thirdpage(request):
    return render (request, 'main/Thirdpage.html')

def fourthpage(request):
    return render (request, 'main/fourthpage.html')

# Создаем верхнее меню
def about(request):
    return render (request, 'main/about.html')

def services(request):
    return render (request, 'main/services.html')

def contacts(request):
    return render (request, 'main/contacts.html')

def terms(request):
    return render (request, 'main/terms.html')

