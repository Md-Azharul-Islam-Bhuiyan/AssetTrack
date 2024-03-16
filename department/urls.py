from django.urls import path, include
from .views import DepartmentView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("list", DepartmentView)

urlpatterns = [
    path("", include(router.urls)),
    # path("/", DepartmentView.as_view(), name="department")
]
