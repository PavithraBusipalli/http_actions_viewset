from rest_framework import serializers
from .models import * 

class Product_cat_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class Product_ModelSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        