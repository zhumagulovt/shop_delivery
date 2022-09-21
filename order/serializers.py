from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):

    TIME_CHOICES = (
        ("12:00", "12:00"),
        ("13:00", "13:00")
    )

    items = OrderItemSerializer(many=True)
    delivery_time = serializers.ChoiceField(choices=TIME_CHOICES)

    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'address', 'delivery_time', 'items']
