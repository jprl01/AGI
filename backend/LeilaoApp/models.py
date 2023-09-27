from django.db import models

# Create your models here.

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_username= models.CharField(max_length=100)
    client_password = models.CharField(max_length=100)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    client_Id = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='+')
    product_Type = models.CharField(max_length=100)
    closed = models.BooleanField()
    product_url = models.CharField(max_length=100)
    actual_value = models.IntegerField()
    product_buyer = models.CharField(max_length=100)
    
