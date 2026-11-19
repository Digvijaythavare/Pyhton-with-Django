from django.http import HttpResponse

def home(request):
    return HttpResponse("Shop Home page")

def Products(request):
    return HttpResponse("Shop Products page")
