from django.contrib import admin
from .models import *


# Register your models here.

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]


admin.site.register(Wishlist)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order)
