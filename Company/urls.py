from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationView, activate, LoginView, LogoutView


router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', activate, name='activate')
]
