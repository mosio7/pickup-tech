import re
from django.shortcuts import render
from django.shortcuts import HttpResponse

def  about(request):
    #return HttpResponse("hi, wellcome to our pickup")
    return render(request , 'about.html')


def  home(request):
    #return HttpResponse("home")
    return render(request , 'home.html')