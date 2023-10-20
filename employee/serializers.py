from rest_framework import serializers
from .models import Employee, EmployeeShifts

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeShifts
        fields = '__all__'