from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import OwnerSerializer, PropertySerializer
from properties.models import Owner, Property


@api_view(['GET', 'POST'])
def owner_list(request):
    if request.method == 'GET':
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def properties(request):
    if request.method == 'GET':
        property_list = Property.objects.all()
        serializer = PropertySerializer(property_list, many=True)
        return Response(serializer.data)


