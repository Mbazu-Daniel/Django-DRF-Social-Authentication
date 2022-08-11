from django.contrib import admin
from .models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
         "user",
        "category",
        "title",
        "status"
    ]
    prepopulated_fields = {
        "slug": [
            "title",
        ],
    }
    search_fields = ["title"]


admin.site.register(Comment)
admin.site.register(Category)
