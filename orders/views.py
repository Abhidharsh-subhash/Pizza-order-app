from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class HelloOrderview(GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Order"},status=status.HTTP_200_OK)
