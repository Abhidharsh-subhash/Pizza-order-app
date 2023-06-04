from django.shortcuts import render,get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .import serializers
from . models import Order
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User=get_user_model()

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
    serializer_class=serializers.OrderDetailSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        serializer=self.serializer_class(instance=order)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,order_id):
        data=request.data
        order=get_object_or_404(Order,pk=order_id)
        serializer=self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UpdateOrderStatus(GenericAPIView):
    serializer_class=serializers.orderStatusUpdateSerializer
    def put(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        data=request.data
        serializer=self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
class UserOrdersView(GenericAPIView):
    serializer_class=serializers.OrderDetailSerializer
    queryset=Order.objects.all()
    def get(self,request,user_id):
        user=User.objects.get(pk=user_id)
        orders=Order.objects.all().filter(customer=user)
        #many=True when Attribute error occurs
        serializer=self.serializer_class(instance=orders,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
class UserOrderDetail(GenericAPIView):
    serializer_class=serializers.OrderDetailSerializer
    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)
        order=Order.objects.filter(customer=user).get(pk=order_id)
        serializer=self.serializer_class(instance=order)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    

