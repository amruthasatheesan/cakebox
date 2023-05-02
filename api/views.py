from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from api.serializers import UserSerializer,CakeSerializers
from api.models import Cakes
from rest_framework import authentication,permissions
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework import serializers



class UsersView(GenericViewSet,CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class CakesView(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    
    serializer_class=CakeSerializers
    queryset=Cakes.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        qs=Cakes.objects.all()

        if "layers" in self.request.query_params:
            lyr=self.request.query_params.get("layers")
            qs=qs.filter(layers=lyr)

        if "shape" in self.request.query_params:
            sh=self.request.query_params.get("shape")
            qs=qs.filter(shape=sh)
            
        return qs
        