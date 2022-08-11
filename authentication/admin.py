from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import TextInput, Textarea, CharField


class UserAdminConfig(admin.ModelAdmin):
    model = User
    search_fields = ["email", "username", "first_name", "auth_provider",]
    list_filter = ["email", "username", "first_name", "is_active", "is_staff"]
    ordering = ["-created_at"]
    readonly_fields = ["auth_provider"]
    list_display = [
        "email",
        "username",
        "auth_provider",
        "is_active",
        "is_staff",
        "is_verified"
    ]

admin.site.register(User, UserAdminConfig)


# from django.contrib import admin

# # Register your models here.
# from .models import User


# class UserAdmin(admin.ModelAdmin):
#     list_display = ["username", "email", , "is_active", "is_staff" ]


# admin.site.register(User, UserAdmin)
