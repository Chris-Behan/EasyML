from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import csv
import pandas as pd
import api.linear_reg as ml


@api_view(['GET', 'POST'])
def create_linear_model(request):
    if request.method == 'GET':
        return Response({"message": "csv file"})
    elif request.method == 'POST':
        features = request.query_params.get("features")
        label = request.query_params.get("label")
        if 'file' in request.data:
            file = request.data['file']
            accuracy, mean_error, model_id = ml.process_file(features=features, label=label, file=file)
        return Response({"accuracy": accuracy,
                         "mean_error": mean_error,
                         "model_id": model_id})

@api_view(['POST'])
def linear_prediction(request):
    return Response("hello")
