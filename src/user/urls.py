from django.urls import path, include
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetCompleteView

from rest_framework import routers

from .views import LoginView, RegisterUserView, ForgotPasswordView

router = routers.DefaultRouter()

router.register(r'register', RegisterUserView, basename='register')

urlpatterns = [
    path('user/', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
