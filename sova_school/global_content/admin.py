from django.contrib import admin
from .models import GlobalContent


class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at", "photos"]


admin.site.register(GlobalContent, imageAdmin)
