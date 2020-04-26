from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World !!!")

def appPage(request):
    return HttpResponse("This is the firstApp page !!!")

def templatePage(request):
    x = {'insert_me' : "This is from views.py"}
    return render(request, "first_app/index.html", context= x)

def imagePage(request):
    return render(request, "first_app/imagePageHtml.html")