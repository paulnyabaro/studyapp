from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'base/home.html')


def room(request):
    return HttpResponse("Room")
