from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getall(request):
    stdata=Studinfo.objects.all()
    serial=StudSerial(stdata,many=True)
    return Response(serial.data)
    
    
