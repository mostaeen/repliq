from rest_framework import serializers
from .models import Device, DeviceLog


class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    logs = DeviceLogSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = '__all__'
