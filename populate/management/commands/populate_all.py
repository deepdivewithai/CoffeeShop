# management/commands/populate_all.py
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Populate data in the correct order'

    def handle(self, *args, **options):
        # List of custom management commands to run in order
        commands_to_run = [
            'populate_products',
            'populate_customers',
            'populate_employees',
        ]

        # Execute each custom command
        for command in commands_to_run:
            call_command(command)

        self.stdout.write(self.style.SUCCESS('Successfully populated data.'))
