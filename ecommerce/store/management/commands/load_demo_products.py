from django.core.management.base import BaseCommand
from store.models import Product, Category

class Command(BaseCommand):
    help = 'Loads demo products into the database'

    def handle(self, *args, **options):
        # Create categories
        electronics, _ = Category.objects.get_or_create(
            name='Electronics',
            slug='electronics'
        )
        clothing, _ = Category.objects.get_or_create(
            name='Clothing',
            slug='clothing'
        )

        # Demo products
        products = [
            {
                'name': 'Smartphone X',
                'slug': 'smartphone-x',
                'description': 'Latest smartphone with advanced features',
                'price': 699.99,
                'discount_price': 599.99,
                'image': 'https://via.placeholder.com/300x300?text=Smartphone',
                'category': electronics,
                'available': True,
                'stock': 10
            },
            {
                'name': 'Wireless Headphones',
                'slug': 'wireless-headphones',
                'description': 'Noise cancelling wireless headphones',
                'current_price': 199.99,
                'old_price': 249.99,
                'image': 'products/headphones.jpg',
                'category': electronics,
                'available': True
            },
            {
                'name': 'Men\'s T-Shirt',
                'slug': 'mens-tshirt',
                'description': 'Comfortable cotton t-shirt',
                'price': 24.99,
                'discount_price': 19.99,
                'image': 'https://via.placeholder.com/300x300?text=T-Shirt',
                'category': clothing,
                'available': True,
                'stock': 20
            },
            {
                'name': 'Women\'s Jeans',
                'slug': 'womens-jeans',
                'description': 'Stylish denim jeans',
                'current_price': 39.99,
                'old_price': 49.99,
                'image': 'products/jeans.jpg',
                'category': clothing,
                'available': True
            }
        ]

        # Create products
        for product_data in products:
            Product.objects.get_or_create(**product_data)

        self.stdout.write(self.style.SUCCESS('Successfully loaded demo products'))