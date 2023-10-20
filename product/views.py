from .models import Product, Inventory
from .serializers import ProductSerializer, InventorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class InventoryListView(ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDetailView(RetrieveDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer