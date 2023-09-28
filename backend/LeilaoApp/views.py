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
# Create your views here.

@csrf_protect
@api_view(['POST'])
@parser_classes([JSONParser])
def addBalance(request,format=None):
    if request.method=='POST':
        client_id_loggedin = request.COOKIES.get('client_id')
        add_balance = request.data.get('balance_value')
        with transaction.atomic():
            client = Client.objects.get(client_id= client_id_loggedin)
            client.balance= client.balance + add_balance
            client.save()

        response= Response({"Added balance successfully"}, status=201)
        return response
    else:
        return Response({"error": "request method fail"}, status=404)
        

@csrf_protect
@api_view(['GET'])
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
        client_id_loggedin = request.COOKIES.get('client_id')
        products = Product.objects.filter(client_id=client_id_loggedin, closed=False)
        print(products)
        serializer = ProductSerializer(products, many=True)
        print(serializer)
        return Response(serializer.data)
    else:
        return Response({"error": "request method fail"}, status=404)
               


@csrf_protect
@api_view(['POST'])
@parser_classes([JSONParser])
def login(request,format=None):
    if request.method == 'POST':
        client_username = request.data.get('client_username')
        client_password = request.data.get('client_password')
        client = Client.objects.get(client_username=client_username,client_password=client_password)
        if client:
            client_serializer = ClientSerializer(client, many=True)
           
            response= Response({"Login Sucess"}, status=201)
            response.set_cookie('client_id',client.client_id)
            return response
        else:
            return Response({"error": "Unknown Client"}, status=404)
    else:
            return Response({"error": "request method fail"}, status=404)

@csrf_protect
@api_view(['GET'])
def logout(request,format=None):
    if request.method == 'GET':
        if request.COOKIES.get('client_id'):
            response= Response({"Logout Sucess"}, status=201)
            response.set_cookie('client_id',{})
            return response
        else:
            return request({"Logout Fail"})
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
        client_id = request.COOKIES.get("client_id")
        cookie_client_id = {'client_id': client_id}
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
def closeProductAuction(request,id, format=None):
    if request.method == 'GET':
        client_id_loggedin = request.COOKIES.get('client_id')
        product = Product.objects.filter(product_id=id,client_Id=client_id_loggedin)
        if product:
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
    

# {
#     "client_username":"teste",
#     "client_password":"1234"
# }
