from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
#this if for swagger and we can define what is the funcitoning of each view
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from . import serializers

# Create your views here.
class HelloAuthview(GenericAPIView):
    @swagger_auto_schema(operation_summary='Hello Auth.')
    def get(self,request):
        return Response(data={"message":"Hello Auth"},status=status.HTTP_200_OK)
    
class UserCreateView(GenericAPIView):
    serializer_class=serializers.UserCreationSerializer
    @swagger_auto_schema(operation_summary='Create a user account.')
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)