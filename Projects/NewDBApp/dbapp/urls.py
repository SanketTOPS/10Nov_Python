from django.contrib import admin
from django.urls import path,include
from dbapp import views

urlpatterns = [
    path('',views.index),
]