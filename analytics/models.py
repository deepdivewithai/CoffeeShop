from django.db import models

class SalesAnalytics(models.Model):
    date = models.DateField(unique=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    product_sold = models.PositiveIntegerField(null=True, default=0)
    customer_count = models.PositiveIntegerField(null=True, default=0)
    employee_performance = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self) -> str:
        return self.date