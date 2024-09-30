# inventory/urls.py
from django.urls import path
from .views import ProductCreateView, ProductDetailView, AddStockView, SellProductView, SalesHistoryView

urlpatterns = [
    path('create-product/', ProductCreateView.as_view(), name='create-product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('add-stock/', AddStockView.as_view(), name='add-stock'),
    path('sell-product/', SellProductView.as_view(), name='sell-product'),
    path('sales-history/', SalesHistoryView.as_view(), name='sales-history'),
]
