from django.db import models

# Create your models here.
class donars(models.Model):
    name=models.CharField(max_length=40)
    blood=models.CharField(max_length=5)
    mobile=models.CharField(max_length=12)
    recovered=models.DateTimeField()
class recipient(models.Model):
    name=models.CharField(max_length=40)
    blood=models.CharField(max_length=5)
    mobile=models.CharField(max_length=12)
    hospital=models.CharField(max_length=30)
