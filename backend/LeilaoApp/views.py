from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_protect

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response

from LeilaoApp.serializers import ClientSerializer
from LeilaoApp.serializers import ProductSerializer

from .models import Client
from .models import Product
# Create your views here.

@csrf_protect
@api_view(['GET'])
def getAllClients(self,request,format=None):
    if request.method == 'GET':
        clients = Client.objects.all()
        print(clients)
        serializer = ClientSerializer(clients, many=True)
        print(serializer)
        return Response(serializer.data)
        
@csrf_protect
@api_view(['GET'])
def showAuctionProducts(self,request,format=None):
    if request.method == 'GET':
        products = Product.objects.all()
        print(products)
        serializer = ProductSerializer(products, many=True)
        print(serializer)
        return Response(serializer.data)
        


@csrf_protect
@api_view(['GET'])
def login(request,username,password,format=None):
    if request.method == 'GET':
        client = Client.objects.filter(client_username=username,client_password=password)
        if client:
            client_serializer = ClientSerializer(client, many=True)
            return Response(client_serializer.data)
        else:
            return Response({"error": "Unknown Client"}, status=404)
    else:
            return Response({"error": "request method fail"}, status=404)

@csrf_protect
@api_view(['POST'])
@parser_classes([JSONParser])
def createClient(request):
    if request.method == 'POST':
        client_serializer = ClientSerializer(data=request.data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response({"message": "Client added successfully"}, status=201)
        else:
            return Response(client_serializer.errors, status=400)






@csrf_protect
@api_view(['GET'])
def hello(request):
    return Response("HELLO WORLD")
    