# inventory/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    unit_measurements = models.JSONField()  # For storing units like {'Pack': 200, 'Carton': 2400}
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    unit_measurement = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.product.name} - {self.unit_measurement}'

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_measurement = models.CharField(max_length=100)
    sale_time = models.DateTimeField(auto_now_add=True)
    profit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Sale: {self.product.name} - {self.unit_measurement}'
