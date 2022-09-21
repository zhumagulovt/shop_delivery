from django.db import models

from products.models import Product


class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя покупателя')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    address = models.TextField(verbose_name='Адрес')
    ordered_date = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')
    ordered = models.BooleanField(default=False, verbose_name='Завершен')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Конечная стоимость")
    delivery_time = models.TimeField(blank=True, verbose_name='Время доставки')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Предмет заказа'
        verbose_name_plural = 'Предметы заказа'
        
