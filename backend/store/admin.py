from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'category', 'slug', 'image')
    list_filter = ('brand', 'category')
    search_fields = ('name', 'brand')
    prepopulated_fields = {'slug': ('name',)}
