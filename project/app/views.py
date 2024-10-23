from django.shortcuts import render 
from .forms import userform , Profileform

def base(request):
    context={}
    context['user'] = userform
    context['profile'] = Profileform
    return render(request, 'base.html',context)