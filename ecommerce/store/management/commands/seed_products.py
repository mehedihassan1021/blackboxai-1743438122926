from django.core.management.base import BaseCommand
from store.models import Product, Category

class Command(BaseCommand):
    help = 'Seed the database with initial products'

    def handle(self, *args, **options):
        # Get or create categories
        electronics, _ = Category.objects.get_or_create(
            slug='electronics',
            defaults={'name': 'Electronics'}
        )
        
        clothing, _ = Category.objects.get_or_create(
            slug='clothing',
            defaults={'name': 'Clothing'}
        )

        # Create products if they don't exist
        Product.objects.get_or_create(
            slug='smartphone',
            defaults={
                'name': 'Smartphone X',
                'description': 'Latest model with great camera',
                'price': 699.99,
                'discount_price': 599.99,
                'image': 'https://via.placeholder.com/300',
                'category': electronics,
                'stock': 10
            }
        )
        
        Product.objects.get_or_create(
            slug='t-shirt',
            defaults={
                'name': 'Cotton T-Shirt',
                'description': 'Comfortable everyday wear',
                'price': 24.99,
                'image': 'https://via.placeholder.com/300',
                'category': clothing,
                'stock': 20
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded products'))