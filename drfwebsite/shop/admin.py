from django.contrib import admin

from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'price', 'is_published', 'published_time', 'cat', 'user', )
    list_filter = ('is_published', 'published_time', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
