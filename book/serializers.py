from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RecipeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeProduct
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    products = RecipeProductSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'
