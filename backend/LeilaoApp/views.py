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
from django.db import transaction

from rest_framework.authentication import TokenAuthentication
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes

# Create your views here.

@csrf_protect
@api_view(['POST'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication, JWTCookieAuthentication])
@permission_classes([IsAuthenticated])
def addBalance(request,format=None):
    print(request.user)
    if request.method=='POST':
        client_username = request.user
        with transaction.atomic():
            client = Client.objects.get(client_username=client_username)
            if client:

                client.balance= client.balance + request.data.get('balance_value')
                client.virtual_balance = client.virtual_balance + request.data.get('balance_value')
                client.save()
                return Response({"message :Added balance successfully"}, status=201)
            else:
                return Response({"error": "Unknown Client"}, status=404)

    else:
        return Response({"error": "request method fail"}, status=404)
        

@csrf_protect
@api_view(['GET'])
@authentication_classes([TokenAuthentication, JWTCookieAuthentication])
@permission_classes([IsAuthenticated])
def getAllClients(request,format=None):
    if request.method=='GET':
        clients = Client.objects.all()
        print(clients)
        serializer = ClientSerializer(clients, many=True)
        print(serializer)
        return Response(serializer.data)
    else:
        return Response({"error": "request method fail"}, status=404)
    

@csrf_protect
@api_view(['GET'])
def showClientAuctionProducts(request,format=None):
    if request.method == 'GET':
        client_username = request.user
        with transaction.atomic():      
        
            products = Product.objects.filter(client_username=client_username, closed=False)
            print(products)
            serializer = ProductSerializer(products, many=True)
            print(serializer)
            return Response(serializer.data)
    else:
        return Response({"error": "request method fail"}, status=404)
               




@api_view(['POST'])
@parser_classes([JSONParser])
@authentication_classes([])
@permission_classes([])
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
def auctionProduct(request,format=None):
    if request.method == 'POST':
        client_username = request.user
        
        with transaction.atomic():
            value = request.data.get('value')
            product_id = request.data.get('product_id')

            client = Client.objects.get(client_username=client_username)
            product = Product.objects.filter(product_id= product_id)
            if product.actual_value <  value and client.virtual_balance >= value:
                old_buyer = Client.objects.get(client_id=product.product_buyer)
                old_buyer.virtual_balance = client.virtual_balance + product.actual_value

                client.virtual_balance = client.virtual_balance - value
                product.actual_value = value
                product.product_buyer = client_id_loggedin

                old_buyer.save()
                product.save()
                client.save()
            else:
                return Response({"message": "Someone already paid more"}, status=201)
            

@csrf_protect
@api_view(['GET'])
def showAuctionProducts(format=None):
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
        client_username = request.user        
        
        cookie_client_id = {'client_username': client_username}
        request_data= {**request.data, **cookie_client_id}
        proc_serializer = ProductSerializer(data=request_data)
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
def closeProductAuction(request,format=None):
    if request.method == 'GET':
        client_username = request.user
        
        with transaction.atomic():
            product = Product.objects.filter(product_id=id,client_Id=client_id_loggedin)
            if product:
                client = Client.objects.get(client_username=client_username)
                client.balance=client.balance + product.actual_value
                client_buyer = Client.objects.get(client_id=client.product_buyer)
                client_buyer.balance = client_buyer.balance - product.actual_value
                client.save()
                client_buyer.save()
                product.save()
                product.closed=True
                
            else:
                return Response({"message": "error"}, status=201)
 

@csrf_protect
@api_view(['GET'])
def home(request):
    response = Response("HOME")
    response.set_cookie('client_id',{})
    return response



@csrf_protect
@api_view(['GET'])
def hello(request):
    return Response("HELLO WORLD")
    

''' {
     "client_username":"teste"
 }'''
