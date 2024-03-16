from django.urls import path, include
from .views import ProvideAssetView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
#This route is used for Asset history. update,create and delete are presents in this route. 
router.register("list", ProvideAssetView)

urlpatterns = [
    path("", include(router.urls)),
]
