from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Product, Category

class Command(BaseCommand):
    help = 'Initialize the e-commerce store with admin and products'

    def handle(self, *args, **options):
        # Create admin user safely
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_superuser': True,
                'is_staff': True
            }
        )
        if created:
            admin.set_password('admin123')
            admin.save()
            self.stdout.write(self.style.SUCCESS('Created admin user'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))

        # Create categories safely
        electronics, e_created = Category.objects.get_or_create(
            slug='electronics',
            defaults={'name': 'Electronics'}
        )
        clothing, c_created = Category.objects.get_or_create(
            slug='clothing',
            defaults={'name': 'Clothing'}
        )

        # Create products safely
        p1, p1_created = Product.objects.get_or_create(
            slug='smartphone',
            defaults={
                'name': 'Smartphone',
                'description': 'Latest model',
                'price': 699.99,
                'discount_price': 599.99,
                'image': 'https://via.placeholder.com/300',
                'category': electronics,
                'stock': 10
            }
        )
        
        p2, p2_created = Product.objects.get_or_create(
            slug='t-shirt',
            defaults={
                'name': 'T-Shirt',
                'description': 'Cotton t-shirt',
                'price': 24.99,
                'image': 'https://via.placeholder.com/300',
                'category': clothing,
                'stock': 20
            }
        )

        self.stdout.write(self.style.SUCCESS('Store initialization complete'))
        self.stdout.write(f'Admin login: admin/admin123')
        self.stdout.write(f'Access admin at: /admin/')