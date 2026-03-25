from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def cart(request):
    return render(request,'cart.html')

def chackout(request):
    return render(request,'chackout.html')

def contact(request):
    return render(request,'contact.html')

def shop(request):
    return render(request,'shop.html')