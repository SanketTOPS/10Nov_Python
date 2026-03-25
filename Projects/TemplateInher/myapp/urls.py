from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [
    path('',home),
    path('about/',about),
    path('contact/',contact),
    
]
