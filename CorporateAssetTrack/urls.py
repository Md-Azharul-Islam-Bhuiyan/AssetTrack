from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include("Company.urls")),
    path('device/', include("device.urls")),
    path('department/', include("department.urls")),
    path('employee/', include("Employee.urls")),
    path('asset_history/', include("assetHistory.urls")),
    
]
