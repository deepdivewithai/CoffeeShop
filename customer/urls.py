from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer_list'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/order_details/', views.OrderDetailView.as_view(), name='order_details'),
    path('feedback/', views.FeedbackView.as_view(), name='customer_feedback'),
]
