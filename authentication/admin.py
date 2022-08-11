from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import TextInput, Textarea, CharField


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ["email", "username", "first_name"]
    list_filter = ["email", "username", "first_name", "is_active", "is_staff"]
    ordering = ["-created_at"]
    list_display = [
        "email",
        "username",
        "auth_provider",
        "created_at",
        "is_active",
        "is_staff",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "first_name",
                )
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                )
            },
        ),
        ("personal", {"fields": ("about",)}),
    )

    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }

    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "email",
                "username",
                "first_name",
                "password",
                "is_active",
                "is_staff",
            ),
        },
    )


admin.site.register(User, UserAdminConfig)


# from django.contrib import admin

# # Register your models here.
# from .models import User


# class UserAdmin(admin.ModelAdmin):
#     list_display = ["username", "email", "auth_provider", "created_at"]


# admin.site.register(User, UserAdmin)
