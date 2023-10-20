from django.db import models
from employee.models import Employee
from product.models import Product

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
order_status = [("pending", "Pending"), ("completed", "Completed")]
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=order_status)
    payment_method = models.CharField(max_length=55)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.customer.name

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate line_total before saving
        self.line_total = self.product.price * self.quantity
        super(OrderDetail, self).save(*args, **kwargs)

class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField()
    comments = models.TextField()