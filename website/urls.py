from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls', namespace='product')),
    path('customer/', include('customer.urls', namespace='customer')),
    path('employee/', include('employee.urls', namespace='employee')),
]