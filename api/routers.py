from .views import EmployeeViewSet, TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'task', TaskViewSet)
