from .models import Employee, EmployeeShifts
from .serializers import EmployeeSerializer, EmployeeShiftSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

class EmployeeListView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ShiftsView(ListCreateAPIView):
    queryset = EmployeeShifts.objects.all()
    serializer_class = EmployeeShiftSerializer