from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html', {'name':'Dinto'})


def add(request):
    x = int(request.POST["num1"])
    y = int(request.POST["num2"])
    res = x + y
    return render(request, 'result.html',{"result":res})

