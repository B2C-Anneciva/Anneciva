from rest_framework import serializers
from product.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'company',
            'category',
            'image',
            'medicine_form',
            'country',
            'company',
            'trade_name_of_the_drug',
            'active_ingredient',
            'composition',
            'pharmacotherapeutic_group',
            'contraindication',
            'pharmacokinetic',
            'storage_condition',
            'expiration',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]
