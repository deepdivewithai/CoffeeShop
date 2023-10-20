# populate/management/commands/populate_employees.py
from django.core.management.base import BaseCommand
from employee.models import Employee  # Import your Employee model

class Command(BaseCommand):
    help = 'Populate employee data'

    def handle(self, *args, **options):
        # Your data population logic goes here
        Employee.objects.create(name='Barista A', role='Barista', contact_information='barista@example.com', hire_date='2023-01-15')
        Employee.objects.create(name='Cashier B', role='Cashier', contact_information='cashier@example.com', hire_date='2023-02-20')
        # Add more employee data as needed

        self.stdout.write(self.style.SUCCESS('Successfully populated employees.'))
