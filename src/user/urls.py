from django.urls import path, include
from . import views
app_name = 'social'
urlpatterns = [
    path(f"api/login/<str:backend>/", views.auth, name="login"),
    path(f"api/complete/<str:backend>/", views.get_token, name='complete'),
    path(f"dashboard/", views.dashboard, name='dashboard')
    ]
