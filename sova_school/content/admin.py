from django.contrib import admin
from django.utils.html import format_html

from .models import Content




class role_inline(admin.TabularInline):
    model = Content
    extra = 1

@admin.register(Content)
class ContentAdminForm(admin.ModelAdmin):
    list_display = ["title", "text", "user", "created_at", "slug", "image_tag" ]
    list_filter = ["title"]
    def image_tag(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.image_url))
        return None

    fieldsets = [
        (None, {"fields": ["title", "text", "image_url"]}),
        ("Permissions", {"fields": ["slug", "user"]}),
    ]


    class Meta:
        model = Content
        fields = '__all__'


    def save_formset(self, request, form, formset, change):
        for object in formset.save():
            object.name = object.name.upper()
        formset.save(commit=True)

    def __str__(self) -> str:
        return f'{self.form}'



