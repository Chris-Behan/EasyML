from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


@api_view(['GET', 'POST'])
def process_file(request):
    if request.method == 'GET':
        return Response({"message": "csv file"})
    elif request.method == 'POST':
        features = request.query_params.get("features")
        label = request.query_params.get("label")
        if 'file' in request.data:
            file = request.data['file']
            print(type(file))
            print("test!!!")
        return Response({"message": "file received",
                         "features": features.split(','),
                         "label": label})
