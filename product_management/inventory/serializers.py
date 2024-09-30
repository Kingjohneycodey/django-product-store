# inventory/serializers.py
from rest_framework import serializers
from .models import Product, Stock, Sale

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'unit_measurements']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'product', 'cost_price', 'quantity', 'unit_measurement']

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'product', 'quantity', 'selling_price', 'unit_measurement', 'sale_time', 'profit']
