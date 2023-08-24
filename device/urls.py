from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, DeviceLogViewSet

router = DefaultRouter()

# API available at http://127.0.0.1:8000/gears/devices/
router.register(r'devices', DeviceViewSet)

# API available at http://127.0.0.1:8000/gears/devicelogs/
router.register(r'devicelogs', DeviceLogViewSet)

urlpatterns = router.urls
