from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def data(request):
    return HttpResponse("<h1>1,2,3,4,5</h1>")

def test(request):
    return HttpResponse("<h1>Проверка работы программы</h1>")


# Create your views here.
