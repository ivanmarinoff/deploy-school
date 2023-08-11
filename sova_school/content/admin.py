from django.contrib import admin
from .models import Content




class role_inline(admin.TabularInline):
    model = Content
    extra = 1

@admin.register(Content)
class ContentAdminForm(admin.ModelAdmin):
    list_display = ["title", "text", "user", "created_at", "slug"]
    list_filter = ["title"]

    fieldsets = [
        (None, {"fields": ["title", "text"]}),
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



class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm
    list_display = ["user", "title", "text", "created_at", "slug"]


