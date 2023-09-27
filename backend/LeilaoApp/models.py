from django.db import models

# Create your models here.

class Client(models.Model):
    ClientId = models.AutoField(primary_key=True)
    client_username= models.CharField(max_length=100)
    Clientpassword = models.CharField(max_length=100)