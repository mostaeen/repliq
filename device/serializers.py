from rest_framework import serializers
from .models import Device, DeviceLog
from company.models import Employee


class DeviceLogSerializer(serializers.ModelSerializer):
    device = serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())
    employee = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all())
    # Set to read-only since it's automatically set
    checked_out = serializers.DateTimeField(read_only=True)
    returned = serializers.DateTimeField(required=False)

    class Meta:
        model = DeviceLog
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    logs = DeviceLogSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = '__all__'
