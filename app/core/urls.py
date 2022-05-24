from django.urls import path
from .views import RegisterAPIView, AuthUserAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('endpoint1', AuthUserAPIView.as_view(), name='user'),
    path('endpoint2', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]