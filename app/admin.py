from django.contrib import admin
from app.models import *


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'discount')
    list_display_links = ('id', 'name', 'description', 'price', 'discount')

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'product', 'quantity', 'price')
    list_display_links = ('id', 'customer_name', 'product', 'quantity', 'price')


admin.site.register(User)
admin.site.register(OldOrder)

