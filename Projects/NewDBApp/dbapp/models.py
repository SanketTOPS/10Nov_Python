from django.db import models

# Create your models here.
class studInfo(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    dob=models.DateField()

