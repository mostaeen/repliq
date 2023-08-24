from django.db import models
from company.models import Employee

# Create your models here.


class Device(models.Model):
    name = models.CharField(max_length=100)


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out = models.DateTimeField()
    returned = models.DateTimeField()
    condition_out = models.TextField()
    condition_returned = models.TextField()
