from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('product/', include('product.urls', namespace='product')),
    path('customers/', include('customer.urls', namespace='customer')),
    path('employees/', include('employee.urls', namespace='employee')),
]