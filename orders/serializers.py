from .models import Order
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):
    size=serializers.CharField(default='SMALL')
    order_status=serializers.CharField(default='PENDING')
    quantity=serializers.IntegerField()

    class Meta:
        model=Order
        fields=['size','order_status','quantity']