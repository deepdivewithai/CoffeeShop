from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_details'),
    path('inventory/', views.InventoryListView.as_view(), name='inventory_list'),
    path('inventory/<int:pk>', views.InventoryDetailView.as_view(), name='inventory_details'),
]
