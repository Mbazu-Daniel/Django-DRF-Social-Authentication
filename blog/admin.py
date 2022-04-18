from django.contrib import admin
from .models import Review, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "slug", "user")
    prepopulated_fields = {
        "slug": ("title",),
    }


admin.site.register(Review)
