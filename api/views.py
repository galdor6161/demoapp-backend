from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_data(request):
    return Response({"message": "Hello from Django!"})

@api_view(['GET'])
def get_more_data(request):
    return Response({"data": "This is more data from Django!"})
