from django.core.management.base import BaseCommand
from analytics.models import SalesAnalytics
from datetime import date

class Command(BaseCommand):
    help = 'View daily sales analytics'

    def handle(self, *args, **options):
        # Retrieve the sales analytics data for today (or any date of interest)
        today = date.today()
        try:
            analytics_data = SalesAnalytics.objects.get(date=today)
            self.stdout.write(self.style.SUCCESS('Sales Analytics for {}:\n'.format(today)))
            self.stdout.write('Total Sales: ${:.2f}'.format(analytics_data.total_sales))
            self.stdout.write('Products Sold: {}'.format(analytics_data.product_sold))
            self.stdout.write('Customer Count: {}'.format(analytics_data.customer_count))
            self.stdout.write('Employee Performance: {:.2f}'.format(analytics_data.employee_performance))
        except SalesAnalytics.DoesNotExist:
            self.stdout.write(self.style.ERROR('No sales analytics data found for {}'.format(today)))
