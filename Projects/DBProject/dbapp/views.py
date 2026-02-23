from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        form=StudForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted!")
        else:
            print(form.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})