from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("__str__", "firstname", "lastname", "phone", "jalali_created_at", "is_active", "is_admin")
    list_filter = ("is_admin", "is_active")
    readonly_fields = ("jalali_created_at", "jalali_updated_at", "jalali_last_login")
    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        ("اطلاعات شخصی", {"fields": ("firstname", "lastname", "email", "image", "jalali_created_at", "jalali_updated_at", "jalali_last_login")}),
        ("دسترسی ها", {"fields": ("is_admin", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("firstname", "lastname", "phone", "password1", "password2"),
            },
        ),
    )
    search_fields = ("firstname", "lastname", "phone")
    ordering = ("-created_at",)
    filter_horizontal = ()


admin.site.unregister(Group)
