from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Cakes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class CakeSerializers(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)  
    class Meta:
        model=Cakes
        fields="__all__"