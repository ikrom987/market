from django.contrib import admin

from control.models import Account, Category, Order, OrderItem, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Account)

admin.site.register(Order)
admin.site.register(OrderItem)