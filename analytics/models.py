from django.db import models

class SalesAnalytics(models.Model):
    date = models.DateField(unique=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    product_sold = models.PositiveIntegerField()
    customer_count = models.PositiveIntegerField()
    employee_performance = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    def __str__(self) -> str:
        return self.date