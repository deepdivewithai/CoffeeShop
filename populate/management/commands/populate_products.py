# populate/management/commands/populate_products.py
from django.core.management.base import BaseCommand
from product.models import Product  # Import your Product model

class Command(BaseCommand):
    help = 'Populate product data'

    def handle(self, *args, **options):
        # Your data population logic goes here
        Product.objects.create(name='Coffee', description='A delicious cup of coffee', price=3.99, category='Coffee')
        Product.objects.create(name='Tea', description='A soothing cup of tea', price=2.99, category='Tea')
        # Add more product data as needed

        self.stdout.write(self.style.SUCCESS('Successfully populated products.'))
