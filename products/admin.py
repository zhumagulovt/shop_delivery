from django.contrib import admin
from django.utils.safestring import mark_safe
from django.conf import settings

from .models import Category, Product


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
