from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet

router = DefaultRouter()

# API available at http://127.0.0.1:8000/companies/
router.register(r'companies', CompanyViewSet)

# API available at http://127.0.0.1:8000/employees/
router.register(r'employees', EmployeeViewSet)

urlpatterns = router.urls
