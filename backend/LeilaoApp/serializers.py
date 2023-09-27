from rest_framework import serializers
from LeilaoApp.models import Client,Product


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=('client_id','client_username','client_password')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('product_id','client_id','product_type','actual_value','product_buyer','product_url','closed')