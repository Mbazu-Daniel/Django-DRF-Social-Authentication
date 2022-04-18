from django.contrib import admin
from product.models import Certificate, Experience, SocialMedia, Contact,Project

# Register your models here.

admin.site.register(Certificate)
admin.site.register(Experience)
admin.site.register(SocialMedia)

admin.site.register(Contact)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "user","title", "duration")
    prepopulated_fields = {
        "slug": ("title",),
    }