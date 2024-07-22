from django.db import models

# Create your models here.

class Product(models.Model):
    user = models.CharField(max_length=50)
    item = models.CharField(max_length=100)
    amount = models.IntegerField()
    
    