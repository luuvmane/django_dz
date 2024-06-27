from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from datetime import date


class Command(BaseCommand):
    help = 'Load initial data for categories and products'

    def handle(self, *args, **kwargs):
        # Создание категорий
        category1, created = Category.objects.get_or_create(name="Electronics", defaults={"description": "Electronic devices and gadgets"})
        category2, created = Category.objects.get_or_create(name="Books", defaults={"description": "Various kinds of books"})
        category3, created = Category.objects.get_or_create(name="Clothing", defaults={"description": "Apparel and accessories"})

        # Создание продуктов
        Product.objects.get_or_create(
            name="Smartphone",
            defaults={
                "description": "Latest model smartphone",
                "category": category1,
                "price": 699,
                "created_at": date.today(),
                "updated_at": date.today(),
                "manufactured_at": date.today()
            }
        )

        Product.objects.get_or_create(
            name="Laptop",
            defaults={
                "description": "High performance laptop",
                "category": category1,
                "price": 1200,
                "created_at": date.today(),
                "updated_at": date.today(),
                "manufactured_at": date.today()
            }
        )

        Product.objects.get_or_create(
            name="Novel",
            defaults={
                "description": "Bestselling novel",
                "category": category2,
                "price": 20,
                "created_at": date.today(),
                "updated_at": date.today(),
                "manufactured_at": date.today()
            }
        )

        Product.objects.get_or_create(
            name="T-Shirt",
            defaults={
                "description": "Comfortable cotton t-shirt",
                "category": category3,
                "price": 15,
                "created_at": date.today(),
                "updated_at": date.today(),
                "manufactured_at": date.today()
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))
