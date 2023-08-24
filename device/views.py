from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from rest_framework import viewsets
from .models import Device, DeviceLog
from .serializers import DeviceSerializer, DeviceLogSerializer
from rest_framework.response import Response
from django.http import response
from rest_framework import status


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        device = serializer.validated_data['device']
        employee = serializer.validated_data['employee']

        # Check if the device is already assigned
        if DeviceLog.objects.filter(device=device, returned__isnull=True).exists():
            return Response({'error': 'Device is already assigned.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(checked_out=timezone.now())

        return Response(serializer.data, status=status.HTTP_201_CREATED)
