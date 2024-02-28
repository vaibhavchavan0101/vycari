from rest_framework import routers

from .views import RegisterUserView

router = routers.DefaultRouter()

router.register(r'register', RegisterUserView, basename='register')
