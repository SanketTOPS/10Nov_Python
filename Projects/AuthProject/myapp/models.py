from django.db import models

# Create your models here.
class userSignup(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    mobile=models.BigIntegerField(max_length=10)