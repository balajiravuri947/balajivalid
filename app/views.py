from django.shortcuts import render

from django.http import HttpResponse
from app.forms import *
# Create your views here.
def valido(request):
    form=NameForm()
    d={'form':form}
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            return HttpResponse(str(form_data.cleaned_data))

    return render(request,'valid.html',d)
