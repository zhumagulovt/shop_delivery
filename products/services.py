from datetime import time
from .models import Order, OrderItem

def create_order(name: str, phone_number: str, address: str, delivery_time: time) -> Order:
    """Создать новый заказ"""
    order = Order.objects.create(
        name=name,
        phone_number=phone_number,
        address=address,
        delivery_time=delivery_time
    )
    return order


def create_order_items(order_items: list, order: Order):
    """Создать предметы для покупки(OrderItem) со списка"""
    for order_item in order_items:
        create_order_item(order_item, order)


def create_order_item(order_item: dict, order: Order):
    """Создать предмет для покупки(OrderItem) и привязать к заказу"""

    OrderItem.objects.create(
        order=order,
        product_id=order_item['product_id'],
        quantity=order_item['quantity']
    )


def set_total_price_of_order(order: Order):
    total = 0
    for item in order.items.all():
        total += item.quantity * item.product.price
    
    order.price = total
    return total