from django.db import models

# Create your models here.
class Newuser(models.Model):
    Username=models.CharField(max_length=100)
    Email=models.CharField(max_length=50)
    Pwd=models.CharField(max_length=20)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=1)
    MartialStatus=models.CharField(max_length=50)