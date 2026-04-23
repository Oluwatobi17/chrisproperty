from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('connect/', views.SendFormEmail.as_view(), name="connect"),
]
