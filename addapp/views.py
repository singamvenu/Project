from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'input.html')
def add(request):
    x=int(request.GET["t1"])
    y=int(request.GET["t2"])
    z=x+y
    return HttpResponse("The sum is:"+str(z))
