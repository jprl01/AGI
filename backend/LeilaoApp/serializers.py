from rest_framework import serializers
from LeilaoApp.models import Client,Product


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=('client_id','client_username','balance','virtual_balance')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('product_id','client_username','product_type','actual_value','product_buyer','product_url','closed')