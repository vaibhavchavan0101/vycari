from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
import uuid

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
    def user_id(self, obj):  
        return obj.id  
    user_id.short_description = "Id"
    
    list_display = ('user_id', 'username', 'email', 'phone', 'bio', 'country', 'gender')
    fieldsets = (
        ('User Info', {'fields': ('username', 'email', 'bio', 'phone', 'password',  'country', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )   
    search_fields = ('username', 'phone')

    ordering = ('username',)

admin.site.register(User, UserAdmin)
