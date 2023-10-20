from django.core.management.base import BaseCommand
from datetime import date
from customer.models import Order, Customer
from employee.models import Employee
from analytics.models import SalesAnalytics
from django.db import models
class Command(BaseCommand):
    help = 'Calculate and store daily sales analytics'

    def handle(self, *args, **options):
        # Calculate the date for which you want to create analytics
        today = date.today()

        # Calculate total sales for the day
        total_sales = Order.objects.filter(order_date__date=today).aggregate(total_sales=models.Sum('total_amount'))['total_sales'] or 0

        # Calculate the number of products sold
        products_sold = Order.objects.filter(order_date__date=today).aggregate(products_sold=models.Sum('orderdetail__quantity'))['products_sold'] or 0

        # Calculate the number of customers served
        customer_count = Customer.objects.count()

        # Calculate employee performance if applicable
        employee_performance = Employee.objects.filter(shifts__shift_date_time__date=today).annotate(
            total_shift_duration=models.Sum('shifts__shift_duration')
        ).aggregate(
            total_shift_duration=models.Sum('total_shift_duration')
        )['total_shift_duration']

        # Create or update the sales analytics record for today
        sales_analytics, created = SalesAnalytics.objects.get_or_create(date=today)
        sales_analytics.total_sales = total_sales
        sales_analytics.products_sold = products_sold
        sales_analytics.customer_count = customer_count
        sales_analytics.employee_performance = employee_performance or 0
        sales_analytics.save()

        self.stdout.write(self.style.SUCCESS('Successfully created or updated sales analytics for today.'))
