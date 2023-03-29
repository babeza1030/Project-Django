from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def hello(request):
    name = 'babe'
    lastname = 'Trisit'
    return render(request,'index.html',{"username":name,"lastnameuser":lastname}) 