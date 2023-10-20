from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=55)
    contact_information = models.TextField()
    hire_date = models.DateField()

    def __str__(self) -> str:
        return self.name
    

class EmployeeShifts(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='shifts')
    shift_date_time = models.DateTimeField()
    shift_duration = models.DurationField()

    def __str__(self) -> str:
        return f"{self.employee.name}'s shift on {self.shift_date_time}"