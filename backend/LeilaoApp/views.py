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
def getAllClients(self,format=None):
    clients = Client.objects.all()
    print(clients)
    serializer = ClientSerializer(clients, many=True)
    print(serializer)
    return Response(serializer.data)
    

@csrf_protect
@api_view(['GET'])
def showClientAuctionProducts(self,request,client_id,format=None):
    if request.method == 'GET':
        products = Product.objects.all(client_id=client_id, closed=False)
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
def createClient(request,format=None):
    if request.method == 'POST':
        client_username = request.data.get('client_username')
        client = Client.objects.filter(client_username=client_username)
        if client:
            return Response({"message": "Client already exist"}, status=201)
        else:
            client_serializer = ClientSerializer(data=request.data)
            if client_serializer.is_valid():
                client_serializer.save()
                return Response({"message": "Client added successfully"}, status=201)
            else:
                return Response(client_serializer.errors, status=400)
    else:
        return Response({"error": "request method fail"}, status=404)

@csrf_protect
@api_view(['POST'])
def auctionProduct(request,value,id,product_buyer,format=None):
    if request.method == 'POST':
        product = Product.objects.filter(product_id= id)
        if product.actual_value < value :
            product.actual_value = value
            product.product_buyer = product_buyer
        else:
            return Response({"message": "Someone already paid more"}, status=201)
            

@csrf_protect
@api_view(['GET'])
def showAuctionProducts(self,format=None):
    products = Product.objects.filter(closed=False)
    print(products)
    serializer = ProductSerializer(products, many=True)
    print(serializer)
    return Response(serializer.data)


@csrf_protect
@api_view(['POST'])
@parser_classes([JSONParser])
def createAuctionProducts(request):
    if request.method == 'POST':
        proc_serializer = ProductSerializer(data=request.data)
        print(proc_serializer)
        if proc_serializer.is_valid():
            proc_serializer.save()
            return Response({"message": "Auction added successfully"}, status=201)
        else:
            return Response(proc_serializer.errors, status=400)
    else:
        return Response({"error": "request method fail"}, status=404)

@csrf_protect
@api_view(['GET'])
def closeProductAuction(self,request,id,id_client, format=None):
    if request.method == 'GET':
        product = Product.objects.filter(product_id=id,client_Id=id_client)
        if product:
            product.closed=True
            
        else:
            return Response({"message": "error"}, status=201)
 





@csrf_protect
@api_view(['GET'])
def hello(request):
    return Response("HELLO WORLD")
    

# {
#     "client_username":"teste",
#     "client_password":"1234"
# }
