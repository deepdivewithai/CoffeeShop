from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_list/<int:pk>', views.ProductDetailView.as_view(), name='product_details'),
    path('inventory/', views.InventoryListView.as_view(), name='inventory_list'),
    path('inventory_list/<int:pk>', views.InventoryDetailView.as_view(), name='inventory_details'),
]
