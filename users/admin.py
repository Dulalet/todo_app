from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustoUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'is_staff',  'is_superuser', 'is_active')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'first_name', 'last_name', 'date_joined')
    ordering = ('email',)


admin.site.register(CustomUser, CustoUserAdmin)
