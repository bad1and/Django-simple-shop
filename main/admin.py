from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] #параметры из моделс которые отображаются
    prepopulated_fields = {'slug': ('name',)} # поля автоматически будут заполнены

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated'] #декторатор
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available'] #изменяемы параметры
    prepopulated_fields = {'slug': ('name',)}