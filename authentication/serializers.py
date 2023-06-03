from .models import User
from rest_framework import serializers


class UserCreationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=25)
    email=serializers.EmailField(max_length=80)
    phone_number=serializers.IntegerField(allow_null=False)
    password=serializers.CharField(min_length=8)

    class Meta:
        model=User
        fields=['username','email','phone_number','password']
    #method to validate the entering details
    def validate(self,attrs):
        username_exists=User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(details="User with username exists")
        
        email_exists=User.objects.filter(username=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(details="User with email exists")
        
        Phonenumber_exists=User.objects.filter(username=attrs['phone_number']).exists()
        if Phonenumber_exists:
            raise serializers.ValidationError(details="User with Phonenumber exists")
        
        return super().validate(attrs)