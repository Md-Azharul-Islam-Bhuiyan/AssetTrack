from django.shortcuts import render
from .models import EmployeeModel
from Employee.serializers import EmployeeSerializer 
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class EmployeeView(viewsets.ModelViewSet):
   queryset = EmployeeModel.objects.all()
   permission_classes = [IsAuthenticated]
   serializer_class = EmployeeSerializer
   
   def get_queryset(self):
        
        queryset = EmployeeModel.objects.filter(company__user= self.request.user)

        return queryset    

