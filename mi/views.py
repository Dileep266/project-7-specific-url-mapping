from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit.html')
def sky(request):
    return HttpResponse('<h1>he is 360 player and current no 1 t20 bastmen in icc rankings</h1>')
