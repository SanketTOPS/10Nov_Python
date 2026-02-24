from django.contrib import admin
from django.urls import path,include
from dbapp import views

urlpatterns = [
   path("",views.index),
   path('showdata/',views.showdata,name='showdata'),
   path('update/<int:id>',views.update,name='update'),
   path('deletedata/<int:id>',views.deletedata,name='deletedata'),
]
