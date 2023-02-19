from rest_framework import serializers
from product.models import Product, Category, Comment, Rating

class RatingSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField()
    class Meta:
        model = Rating
        fields = [
            'product_id',
            # 'user',
            'star',
        ]
class ProductSerializer(serializers.ModelSerializer):

    rating = RatingSerializer(many=True)
    class Meta:
        model = Product
        fields = [
            'name',
            'company',
            'price',
            'medicine_form',
            'rating',
        ]

class CommentSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField()
    class Meta:
        model = Comment
        fields = [
            'product_id',
            'comment',
            # 'user'
        ]



class ProductDetailSerializer(serializers.ModelSerializer):

    comment = CommentSerializer(many=True)
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
            'comment',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]

