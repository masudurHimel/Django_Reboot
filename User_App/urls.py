from django.urls import path
from User_App import views

urlpatterns = [
    path('', views.index, name = "User Index"),  
    path('registration/', views.registration, name = "User Registration"),
    
]   
