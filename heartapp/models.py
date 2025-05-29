from django.db import models
# Create your models here.

# create table
class hearts(models.Model):
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=50, default='1') 
    chp = models.CharField(max_length=50, default='1') 
    rbp = models.CharField(max_length=50, default='1')
    chl = models.CharField(max_length=50, default='1') 
    fb = models.CharField(max_length=50, default='1') 
    ecg = models.CharField(max_length=50, default='1') 
    mhr = models.CharField(max_length=50, default='1') 
    ex = models.CharField(max_length=50, default='1')
    olp = models.CharField(max_length=50, default='1')
    sl = models.CharField(max_length=50, default='1')
    nm = models.CharField(max_length=50, default='1')
    ts = models.CharField(max_length=50, default='1') 
    result = models.CharField(max_length=50,default='1')