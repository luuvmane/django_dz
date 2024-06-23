from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Отображение id, наименования и описания
    search_fields = ('name', 'description')  # Поиск по наименованию и описанию


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # Отображение id, названия, цены и категории
    list_filter = ('category',)  # Фильтрация по категории
    search_fields = ('name', 'description', 'category__name')  # Поиск по названию, описанию и имени категории
