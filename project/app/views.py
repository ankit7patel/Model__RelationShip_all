from django.shortcuts import render 
from .forms import userform , Profileform

def base(request):
    context={}
    context['user'] = userform
    context['profile'] = Profileform

    my_list=[]

    return render(request, 'base.html',context)


def userdata(request):
    if request.method=="POST":
        form=userform(request.POST)
        print(form)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            contact=form.cleaned_data['contact']
            address=form.cleaned_data['address']
            print(name)
            print(email)
            print(contact)
            print(address)
            form.save()
            context={}
            context['user'] = userform
            context['profile'] = Profileform

    return render(request, 'base.html')


def profiledata(request):
    if request.method=="POST":
        form=Profileform(request.POST)
        print(form)
        if form.is_valid():
            name=form.cleaned_data['name']
            quli=form.cleaned_data['quli']
            expe=form.cleaned_data['expe']
            skills=form.cleaned_data['skills']
            other=form.cleaned_data['other']
            print(name)
            print(quli)
            print(expe)
            print(skills)
            print(other)
            form.save()


    return render(request, 'base.html')
