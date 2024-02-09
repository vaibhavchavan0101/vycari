"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from . import settings
from django.conf.urls.static import static
from drf_yasg import openapi


# schema_view = get_swagger_view(title='vycari API')
schema_view = get_schema_view(
    openapi.Info(
        title="vycari API",
        default_version='v1',
        description="vycari API",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    urlconf='social',
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [  # pylint: disable=C0103
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('drf-auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
