from django.db import models

# Create your models here.

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_username= models.CharField(max_length=100)
    client_password = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)
    virtual_balance = models.IntegerField(default=0)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='+')
    product_type = models.CharField(max_length=100)
    closed = models.BooleanField(default=False)
    product_url = models.CharField(max_length=100)
    actual_value = models.IntegerField()
    product_buyer = models.CharField(max_length=100,default="")



'''{ 
    "product_type" : "camisa",
    "closed" : false,
    "product_url" : "models.CharField(max_length=100)",
    "actual_value" : 200,
    "product_buyer" : "zeric"
}'''