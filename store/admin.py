from django.contrib import admin

from .models import Address, Category, Product, Customer, Cart, CartItem, Discount , Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'category', 'unit_price', 'inventory', 'datetime_created',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'title','datetime_created',]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [ 'first_name','last_name','email', 'phone_number']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [ 'customer','province','city',]