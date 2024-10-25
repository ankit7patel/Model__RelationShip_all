from django.urls import path
from app import views

urlpatterns = [
    path('',views.base),
    path('userdata/',views.userdata,name="userdata"),
    path('profiledata/',views.profiledata,name='profiledata')

    

]