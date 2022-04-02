from django.contrib import admin
from blog import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "slug", "author")
    prepopulated_fields = {
        "slug": ("title",),
    }

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    verbose_name = "Categories"
