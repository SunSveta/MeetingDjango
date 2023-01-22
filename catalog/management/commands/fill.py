from django.core.management import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):

    def handle(self, *args, **options):
        products = [
            {'product_name': 'Апельсин', 'description': 'Южный', 'image': '', 'category_id': '1', 'price': '900',
             'date_create': '2023-01-19 20:15:00+01', 'date_update': '2023-01-22 23:02:00+01'},
            {'product_name': 'Слива', 'description': 'Слива лиловая, спелая, садовая', 'image': '', 'category_id': '1',
             'price': '1500',
             'date_create': '2023-01-19 20:15:00+01', 'date_update': '2023-01-22 23:02:00+01'},
            {'product_name': 'Малина', 'description': 'Вдаль меня манила', 'image': '', 'category_id': '2',
             'price': '2000',
             'date_create': '2023-01-19 20:15:00+01', 'date_update': '2023-01-22 23:02:00+01'},
            {'product_name': 'Киви', 'description': 'Оказывается это ягода', 'image': '', 'category_id': '2',
             'price': '1200',
             'date_create': '2023-01-19 20:15:00+01', 'date_update': '2023-01-22 23:02:00+01'},
        ]

        categories = [
            {'category_name': 'Фрукты', 'description': 'Вкусные и полезные источники витаминов и хорошего настроения!'},
            {'category_name': 'Ягоды', 'description': 'Маленькие вкусные штуки'},
        ]

        products_list = []
        categories_list = []

        for item in products:
            products_list.append(Product(**item))

        for item in categories:
            categories_list.append(Category(**item))

        Product.objects.all().delete()
        Product.objects.bulk_create(products_list)

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_list)


