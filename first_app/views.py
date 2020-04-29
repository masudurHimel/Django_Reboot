from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage, Topic, AccessDate
from first_app import forms

# Create your views here.

def index(request):
    webpg = AccessDate.objects.order_by('date')
    webpageDict = {'access_record': webpg} 
    return render(request, "index.html", context = webpageDict)

def appPage(request):
    return HttpResponse("This is the firstApp page !!!")

def templatePage(request):
    x = {'insert_me' : "This is from views.py"}
    return render(request, "first_app/templatePage.html", context= x)

def imagePage(request):
    return render(request, "first_app/imagePageHtml.html")


def formPageView(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Hoise")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

            
        
                        

    x = {'form': form}
    return render(request, "form_page.html", context = x)