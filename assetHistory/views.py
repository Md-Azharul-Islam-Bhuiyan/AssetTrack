from datetime import timedelta, datetime
from django.shortcuts import render, redirect
from .serializers import AssetHistorySerializer
from .models import AssetHistory
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status






class ProvideAssetView(viewsets.ModelViewSet):
    queryset=AssetHistory.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AssetHistorySerializer
    
    def get_queryset(self):
        # Filter AssetHistory objects
        queryset = AssetHistory.objects.filter(account= self.request.user)

        return queryset 

    def create(self, request, *args, **kwargs):
        # Create a serializer instance with the request data.
        serializer = self.get_serializer(data=request.data)

        # Check if the serializer data is valid, raising an exception if not.
        serializer.is_valid(raise_exception=True)

        # Set the Company's registered user before saving
        serializer.validated_data['account'] = request.user
        serializer.validated_data['historyType'] = 1

        # Calculate the due date based on the provided date.
        provide_date = serializer.validated_data.get('provide_date') 
        due = provide_date + timedelta(days=730)
        serializer.validated_data['due_date'] = due

        # Save the serializer instance to create the new AssetHistory object.
        self.perform_create(serializer)

         # Get the success headers.
        headers = self.get_success_headers(serializer.data)

        # Return a response with the serialized data, indicating a successful creation.
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



