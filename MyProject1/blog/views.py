from django.http import HttpResponse

def home(request):
    return HttpResponse("Blog Home page")

def About(request):
    return HttpResponse("Blog About page")

# Create your views here.
