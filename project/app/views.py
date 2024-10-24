from django.shortcuts import render 
from .forms import userform , Profileform

def base(request):
    context={}
    context['user'] = userform
    context['profile'] = Profileform
    return render(request, 'base.html',context)

def userdata(request):
    if request.method=="POST":
        form=userform(request.POST)
        print(form)
        if form.is_valid():
            # name=request.cleaned_data['name']
            # email=request.cleaned_data['email']
            # contact=request.cleaned_data['contact']
            # address=request.cleaned_data['address']
            # print(name)
            # print(email)
            # print(contact)
            # print(address)
            form.save()

    # return render(request, 'userdata')