from django.contrib import admin

from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'phone_number', 'ordered', 
        'ordered_date', 'total_price', 'delivery_time'
    )
    list_display_links = ('id', 'name', 'phone_number')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity')
