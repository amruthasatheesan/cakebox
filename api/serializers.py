from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Cakes,Cart,Orders,Reviews


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True) 
    class Meta:
        model=Reviews
        fields=["id","user","comment","rating"]
    
class CakeSerializers(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)  
    cake_review=ReviewSerializer(read_only=True,many=True)
    class Meta:
        model=Cakes
        fields="__all__"

class CartSerializers(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)  
    user=serializers.CharField(read_only=True)  
    created_date=serializers.CharField(read_only=True)  
    status=serializers.CharField(read_only=True)  
    class Meta:
        model=Cart
        # fields=["quantity"]
        exclude=("cake",)


class CartListSerializers(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)  
    user=serializers.CharField(read_only=True)  
    created_date=serializers.CharField(read_only=True)  
    status=serializers.CharField(read_only=True)  
    class Meta:
        model=Cart
        fields="__all__"



class OrderSerializer(serializers.ModelSerializer):
    cake=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    expected_deliverydate=serializers.CharField(read_only=True)
    class Meta:
        model=Orders
        fields=["cake","user","created_date","status","expected_deliverydate","address","matter"]