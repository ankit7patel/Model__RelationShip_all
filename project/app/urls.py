from django.shortcuts import render

# Create your views here.
from django.urls import path
from django.contrib import admin
from app import views

urlpatterns = [
    path('',views.base),
    path('', admin.site.urls),
    path('userdata/',views.userdata,name="userdata")

    

]