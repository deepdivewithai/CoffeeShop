from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_in_stock = models.PositiveIntegerField()
    reorder_point = models.PositiveIntegerField()
    supplier_information = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.product.name