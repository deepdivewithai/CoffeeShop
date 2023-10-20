from django.contrib import admin
from .models import Customer, Order, OrderDetail, Feedback

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Feedback)