from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.
def usdf(request):

    return render(request, 'usdf.html',{"data":"Hai hello"})


from app.forms import *


def validate(request):

    form = userform()


    if request.method == 'POST':


        UD = userform(request.POST)
        
        if UD.is_valid():
            return HttpResponse("data validated")

        else:
            return HttpResponse("not validated")

    return render(request,'validators.html',{'form':form})

