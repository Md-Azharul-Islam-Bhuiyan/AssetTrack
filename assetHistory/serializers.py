from rest_framework import serializers
from .models import AssetHistory


class AssetHistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AssetHistory
        fields = ['device', 'employee','condition_out', 'provide_date']

