# inventory/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Stock, Sale
from .serializers import ProductSerializer, StockSerializer, SaleSerializer

class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class AddStockView(APIView):
    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SellProductView(APIView):
    def post(self, request):
        sales = request.data.get('sales', [])
        total_profit = 0
        for sale_data in sales:
            product_id = sale_data['product']
            product = Product.objects.get(id=product_id)
            quantity = sale_data['quantity']
            unit = sale_data['unit_measurement']
            selling_price = sale_data['selling_price']
            stock_items = Stock.objects.filter(product=product, unit_measurement=unit).order_by('id')

            for stock in stock_items:
                if quantity <= stock.quantity:
                    stock.quantity -= quantity
                    stock.save()
                    break
                else:
                    quantity -= stock.quantity
                    stock.quantity = 0
                    stock.save()

            profit = selling_price - stock.cost_price
            total_profit += profit * quantity

            Sale.objects.create(
                product=product,
                quantity=sale_data['quantity'],
                selling_price=selling_price,
                unit_measurement=unit,
                profit=profit,
            )

        return Response({"message": "Products sold successfully", "total_profit": total_profit})

class SalesHistoryView(APIView):
    def get(self, request):
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)
