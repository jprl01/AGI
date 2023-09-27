from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parses import JSONParser

from django.views.decorators.csrf import csrf_protect

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response

from LeilaoApp.serializers import ClientSerializer

from .models import Client
# Create your views here.

# admin restriction
# TODO ip restriction
@csrf_protect
@api_view(['GET'])
def getAllClients(self, request, format=None):
    
    '''if request.method == 'GET':
        clients = Client.objects.all()
        print(clients)
        serializer = ClientSerializer(clients, many=True)
        print(serializer)
        return Response(serializer.data)
        '''


