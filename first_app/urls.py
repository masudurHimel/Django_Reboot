from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.appPage, name = "FirstApp Page"),
    path('template/', views.templatePage, name = "Template Page")  
]