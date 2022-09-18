from rest_framework import serializers

from .models import Category, Product, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['product', 'amount']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'address', 'orders']