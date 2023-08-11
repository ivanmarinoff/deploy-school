from django.contrib import admin
from .models import GlobalContent


@admin.register(GlobalContent)
class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at", "photos"]
    list_filter = ["title", "created_at", "updated_at"]
    search_fields = ['title']
    ordering = ['-created_at']


# admin.site.register(GlobalContent, imageAdmin)
