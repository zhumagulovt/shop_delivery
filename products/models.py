from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='images/categories/')

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
