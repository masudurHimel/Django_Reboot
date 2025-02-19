"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from first_app import views


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('formPage/', views.formPageView , name ='Form Page'),
    path('', views.index, name = 'Index'),
    path('firstApp/', include("first_app.urls")),
    path('topicAdd/', views.topicAddView, name = "Topic Add"),
    path('userapp/',include("User_App.urls")),
]   
