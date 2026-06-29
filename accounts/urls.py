from django.urls import path

from .views import ChangePasswordAPIView, LoginAPIView, LogoutAPIView, ProfileAPIView, RegisterAPIView, StudentOnlyAPIView, UpdateProfileAPIView

from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),

    path(
    "login/",
    LoginAPIView.as_view(),
    name="login",
    ),

    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="refresh",
    ),
    
    path(
    "profile/",
    ProfileAPIView.as_view(),
    name="profile",
    ),

    path(
    "profile/update/",
    UpdateProfileAPIView.as_view(),
    name="update-profile",
    ),
    path(
    "change-password/",
    ChangePasswordAPIView.as_view(),
    name="change-password",
    ),
    path(
    "logout/",
    LogoutAPIView.as_view(),
    name="logout",
    ),
    path(
    "student-only/",
    StudentOnlyAPIView.as_view(),
    name="student-only",
    ),
]