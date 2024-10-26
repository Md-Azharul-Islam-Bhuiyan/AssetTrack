from django.shortcuts import render
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class DepartmentView(viewsets.ModelViewSet):
    
    queryset = Department.objects.all() #Find all objects of the department
    permission_classes = [IsAuthenticated] #Only Authenticated user can access 
    serializer_class = DepartmentSerializer  

