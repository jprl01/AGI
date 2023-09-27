from rest_framework import serializers
from LeilaoApp.models import Client,Product


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=('client_Id','client_username','Client_password')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('product_id','client_Id','product_Type','actual_value','product_buyer','product_url','closed')