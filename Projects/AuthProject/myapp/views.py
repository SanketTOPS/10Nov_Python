from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.
def home(request):
    user=request.session.get("user")
    name=request.session.get("name")
    return render(request,'home.html',{'user':user,'name':name})

def login(request):
    if request.method=='POST':
        em=request.POST['email']
        pa=request.POST['password']
        
        user=userSignup.objects.filter(email=em,password=pa)
        uid=userSignup.objects.get(email=em)
        print(uid.fullname)
        if user:
            print("Login Successfully!")
            request.session["user"]=em #generate session
            request.session['name']=uid.fullname
            return redirect('home')
        else:
            print("Error!")    
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'signup.html')

def userlogout(request):
    logout(request)
    return redirect('/')
    