from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
  path('',views.login),
  path('signup/',views.signup,name='signup'),
  path('home/',views.home,name='home'),
]
