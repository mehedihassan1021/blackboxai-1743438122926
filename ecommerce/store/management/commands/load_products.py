from django.core.management.base import BaseCommand
from store.models import Product, Category

class Command(BaseCommand):
    help = 'Load basic demo products'

    def handle(self, *args, **options):
        # Create categories
        electronics = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )
        
        clothing = Category.objects.create(
            name='Clothing', 
            slug='clothing'
        )

        # Create sample products
        Product.objects.create(
            name='Smartphone',
            slug='smartphone',
            description='Latest model smartphone',
            price=699.99,
            discount_price=599.99,
            image='https://via.placeholder.com/300',
            category=electronics,
            stock=10
        )
        
        Product.objects.create(
            name='T-Shirt',
            slug='t-shirt', 
            description='Cotton t-shirt',
            price=24.99,
            image='https://via.placeholder.com/300',
            category=clothing,
            stock=20
        )

        self.stdout.write(self.style.SUCCESS('Added 2 demo products'))