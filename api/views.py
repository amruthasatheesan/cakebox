from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from api.serializers import UserSerializer,CakeSerializers,CartSerializers,CartListSerializers,OrderSerializer,ReviewSerializer
from api.models import Cakes,Cart,Reviews,Orders
from rest_framework import authentication,permissions
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action



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
    
    @action(methods=["post"],detail=True)
    def addto_cart(self,request,*args,**kwargs):
            cake=self.get_object()
            serializers=CartSerializers(data=request.data)
            if serializers.is_valid():
                qs=Cart.objects.create(cake=cake,user=request.user,quantity=serializers.validated_data.get("quantity"))
                serializers=CartSerializers(qs)
                return Response(data=serializers.data)
            return Response(data=serializers.errors)
    
    
    @action(methods=["post"],detail=True)
    def make_order(self,request,*args,**kwargs):
        cake=self.get_object()
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cake=cake,user=request.user)
           
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        serializers=ReviewSerializer(data=request.data)
        id=kwargs.get("pk")
        cak=Cakes.objects.get(id=id)
        user=request.user
        if serializers.is_valid():
            serializers.save(user=user,cake=cak)
            return Response(data=serializers.data)
        else:
            return Response(data=serializers.errors)
    
class CartListView(GenericViewSet,ListModelMixin):
    serializer_class=CartListSerializers
    queryset=Cart.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


class OrderListView(GenericViewSet,ListModelMixin):
    serializer_class=OrderSerializer
    queryset=Orders.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


class ReviewListView(GenericViewSet,ListModelMixin):
    serializer_class=ReviewSerializer
    queryset=Reviews.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]