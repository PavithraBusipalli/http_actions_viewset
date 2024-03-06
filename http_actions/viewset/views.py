from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class ProductCategory_JsonData(ViewSet):
    def list(self,request):
        PCO = ProductCategory.objects.all()
        PJSO = Product_cat_ModelSerializer(PCO,many = True)
        return Response(PJSO.data)
    
    def retrieve(self,request,pk):
        PCO = ProductCategory.objects.get(pc_id=pk)
        PJSO = Product_cat_ModelSerializer(PCO)
        return Response(PJSO.data)
    
    def create(self,request):
        JD = request.data
        PJSO = Product_cat_ModelSerializer(data=JD)
        if PJSO.is_valid():
            PJSO.save()
            return Response({'create':'Success'})
        return Response({'create':'fail'})
    def update(self,request,pk):
        PCO = ProductCategory.objects.get(pk=pk)
        PJSO = Product_cat_ModelSerializer(PCO,data=request.data)
        if PJSO.is_valid():
            PJSO.save()
            return Response({'update':'success'})
        return Response({'update':'fail'})
    def partial_update(self,request,pk):
        PCO = ProductCategory.objects.get(pk=pk)
        PJSO = Product_cat_ModelSerializer(PCO,request.data,partial=True)
        if PJSO.is_valid():
            PJSO.save()
            return Response({'partial_update':'Success'})
        return Response({'Partial_update':'fail'})
    def destroy(self,request,pk):
        ProductCategory.objects.get(pk=pk).delete()
        return Response({'delete':'Data is deleted'})
