from django.contrib import admin
from .models import *


# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductRateInline(admin.TabularInline):
    model = ProductRate
    extra = 0


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 0


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductColorInline, ProductSizeInline, ProductRateInline]
    filter_horizontal = ('tags',)


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('font_type', 'parent_category')
    list_display = ('id', 'name', 'parent_category')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
