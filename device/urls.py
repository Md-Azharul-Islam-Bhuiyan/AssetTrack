from django.urls import path, include
from .views import DeviceView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register("list", DeviceView)

urlpatterns = [
    path("", include(router.urls)),
    # path("/", DeviceView.as_view(), name="device")
]


