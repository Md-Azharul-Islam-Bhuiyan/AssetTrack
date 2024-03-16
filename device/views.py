from django.shortcuts import render
from .models import DeviceModel
from .serializers import DeviceSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class DeviceView(viewsets.ModelViewSet):
    
    queryset = DeviceModel.objects.all()
    permission_classes = [IsAuthenticated] #Only Authenticated user can access 
    serializer_class = DeviceSerializer


    def get_queryset(self):
        
        queryset = DeviceModel.objects.filter(company__user= self.request.user) #Filter the objects of Specific Company

        return queryset       

