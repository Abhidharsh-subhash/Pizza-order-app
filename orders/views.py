from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .import serializers
from . models import Order
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class HelloOrderview(GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Order"},status=status.HTTP_200_OK)

#this method is to create the order and list our order 
class OrderCreateListView(GenericAPIView):
    serializer_class=serializers.OrderCreationSerializer
    queryset=Order.objects.all()
    permission_classes=[IsAuthenticated]
    def get(self,request):
        orders=Order.objects.all()
        serialzer=self.serializer_class(instance=orders,many=True)
        return Response(data=serialzer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        user=request.user
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#this method is to get,update and delete sepcific order
class OrderDetailView(GenericAPIView):
    def get(self,request,order_id):
        pass

    def put(self,request,order_id):
        pass

    def delete(self,request,order_id):
        pass

