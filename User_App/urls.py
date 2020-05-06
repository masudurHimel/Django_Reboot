from django.urls import path
from User_App import views

urlpatterns = [
    path('', views.index, name = "User_Index"),  
    path('registration/', views.registration, name = "User Registration"),
    path('login/', views.user_login, name = 'user_login'),
    path('special/', views.special, name = 'special'),
    path('logout/', views.user_logout, name = 'user_logout'),

]   
