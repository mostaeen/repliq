from django.db import models
from company.models import Employee

# Create your models here.


class Device(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out = models.DateTimeField()
    returned = models.DateTimeField(null=True, blank=True)
    condition_out = models.TextField(blank=True)
    condition_returned = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.device
