from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='images/categories/', verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    amount = models.IntegerField(default=0, verbose_name='В наличии')
    image = models.ImageField(upload_to='images/products/')

    # def image_tag(self):
    #     if self.image != '':
    #         return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.image))
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя покупателя')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    address = models.TextField(verbose_name='Адрес')
    ordered_date = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')
    ordered = models.BooleanField(default=False, verbose_name='Завершен')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Конечная стоимость")
    delivery_time = models.TimeField(blank=True, verbose_name='Время доставки')

    # @property
    # def total_price(self):
    #     total = 0
    #     for item in self.items.all():
    #         total += item.quantity * item.product.price
    #     return total
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