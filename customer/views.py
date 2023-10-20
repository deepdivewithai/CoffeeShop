from .models import Customer, Order, OrderDetail, Feedback
from .serializers import CustomerSerializer, OrderSerializer, OrderDetailSerializer, FeedbackSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

class CustomerListView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderDetailView(ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class FeedbackView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer