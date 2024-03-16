from django.shortcuts import render
from .models import EmployeeModel
from Employee.serializers import EmployeeSerializer 
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class EmployeeView(viewsets.ModelViewSet):
   queryset = EmployeeModel.objects.all()
   permission_classes = [IsAuthenticated] # Define permission classes to ensure only authenticated users can access this view.
   serializer_class = EmployeeSerializer
   
   def get_queryset(self):
        # Filter EmployeeView objects
        queryset = EmployeeModel.objects.filter(company__user= self.request.user)

        return queryset    

