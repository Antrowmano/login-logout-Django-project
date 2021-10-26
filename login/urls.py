
from django.contrib import admin
from django.urls import path 
from login import views


urlpatterns = [
     path('', views.registration, name='registration'),
     path('index/', views.index, name='index'),
     path('login/', views.login, name='login'),
]