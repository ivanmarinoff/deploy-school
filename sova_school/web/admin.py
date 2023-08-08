from django.contrib import admin
from .models import WEBContent


@admin.register(WEBContent)
class imageAdmin(admin.ModelAdmin):
    pass






