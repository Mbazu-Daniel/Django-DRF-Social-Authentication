from django.contrib import admin
from .models import PostReview, Post


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "slug", "author")
    prepopulated_fields = {
        "slug": ("title",),
    }


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     verbose_name = "Categories"

admin.site.register(PostReview)
