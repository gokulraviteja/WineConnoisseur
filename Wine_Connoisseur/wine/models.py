from django.db import models

# Create your models here.

class testwine(models.Model):
    country=models.CharField(max_length=30)
    price=models.CharField(max_length=10)
    region1=models.CharField(max_length=30)


class winedata(models.Model):
    country=models.CharField(max_length=30,default="not-available")
    description=models.CharField(max_length=3000,default="not-available")
    designation=models.CharField(max_length=3000,default="not-available")
    points=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    province=models.CharField(max_length=300,default="not-available")
    region_1=models.CharField(max_length=300,default="not-available")
    region_2=models.CharField(max_length=300,default="not-available")
    variety=models.CharField(max_length=300,default="not-available")
    winery=models.CharField(max_length=300,default="not-available")
