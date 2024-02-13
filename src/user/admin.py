from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    """
    Admin configuration for managing UserAdmin instances.

    Attributes:
    list_display (tuple): Fields to be displayed in the list view of the admin interface.
    fieldsets (tuple): Fieldsets to organize fields in the detail view of the admin interface.
    search_fields (tuple): Fields to be searched in the admin interface.
    ordering (tuple): Ordering of objects in the admin interface list view.
    registred UserAdmin on admin site.
    """

    list_display = ('username', 'email', 'phone', 'bio', 'country', 'gender')
    fieldsets = (
        ('User Info', {'fields': ('username', 'email', 'bio', 'phone', 'password',  'country', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('username', 'phone')

    ordering = ('username',)

admin.site.register(User, UserAdmin)
