from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'company',
            'category',
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

