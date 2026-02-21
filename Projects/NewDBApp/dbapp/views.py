from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST': #TRUE
        form=studForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted")
        else:
            print(form.errors)
    return render(request,'index.html')