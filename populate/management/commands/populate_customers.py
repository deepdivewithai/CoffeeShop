# populate/management/commands/populate_customers.py
from django.core.management.base import BaseCommand
from customer.models import Customer  # Import your Customer model

class Command(BaseCommand):
    help = 'Populate customer data'

    def handle(self, *args, **options):
        # Your data population logic goes here
        Customer.objects.create(name='John Doe', email='johndoe@example.com', phone_number='123-456-7890', address='123 Main St')
        Customer.objects.create(name='Jane Smith', email='janesmith@example.com', phone_number='987-654-3210', address='456 Elm St')
        # Add more customer data as needed

        self.stdout.write(self.style.SUCCESS('Successfully populated customers.'))
