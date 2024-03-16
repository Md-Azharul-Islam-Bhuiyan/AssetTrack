from django.urls import path, include
from .views import EmployeeView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("list", EmployeeView)

urlpatterns = [
    path("", include(router.urls)),
    # path("/", EmployeeView.as_view(), name="employee")
]
