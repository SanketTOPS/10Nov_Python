from django.contrib import admin
from .models import *

# Register your models here.
class studdata(admin.ModelAdmin):
    ordering=["id"]
    list_display=['id','name','email','dob']



admin.site.register(studinfo,studdata)