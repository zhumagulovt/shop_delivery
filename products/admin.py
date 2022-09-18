from django.contrib import admin
from django.utils.safestring import mark_safe
from django.conf import settings

from .models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    readonly_fields = ('image_tag', )
    def image_tag(self, obj):
        if obj.image != '':
            return mark_safe('<img src="%s%s" width="200" height="200" />' % (f'{settings.MEDIA_URL}', obj.image))



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'amount')
    list_display_links = ('id', 'name')


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
