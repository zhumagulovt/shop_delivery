# Generated by Django 4.0.5 on 2022-09-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_order_delivery_time_order_total_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='images/categories/', verbose_name='Фото'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]