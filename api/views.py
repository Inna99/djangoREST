from django.shortcuts import render
from rest_framework import viewsets


from .serializers import TaskSerializer, EmployeeSerializer
from .models import Task, Employee


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

