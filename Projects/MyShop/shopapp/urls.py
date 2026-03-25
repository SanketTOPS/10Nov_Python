from django.contrib import admin
from django.urls import path,include
from shopapp import views

urlpatterns = [
   path('',views.index),
   path('cart/',views.cart),
   path('chackout/',views.chackout),
   path('contact/',views.contact),
   path('shop/',views.shop),
]