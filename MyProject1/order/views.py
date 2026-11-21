from django.http import HttpResponse

def Sell(request):
    return HttpResponse("Order sell page")

def Purchase(request):
    return HttpResponse("Order purchase page")