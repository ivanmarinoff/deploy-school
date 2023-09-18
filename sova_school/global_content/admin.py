from django.contrib import admin
from django.utils.html import format_html

from .models import GlobalContent



class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "created_at", "video_tag", "image_tag"]
    list_filter = ["title", "created_at", "updated_at"]
    search_fields = ['title']
    ordering = ['-created_at']

    def image_tag(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.image_url))
        return None

    def video_tag(self, obj):
        if obj.video:
            return format_html('<video src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.video.url))
        return None

    # list_display = ['name', 'image_tag', ]


admin.site.register(GlobalContent, imageAdmin)
