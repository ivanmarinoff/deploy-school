from django.contrib import admin
from .models import Content, UserAnswers


class ContentAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "user_choices", "created_at", "updated_at"]

    def save_formset(self, request, form, formset, change):
        for object in formset.save(): # Here
            object.name = object.name.upper()
        formset.save(commit=True)

class UserAnswersAdmin(admin.ModelAdmin):
    list_display = ["user", "content", "updated"]

    def save_formset(self, request, form, formset, change):
        for object in formset.save(): # Here
            object.name = object.name.upper()
        formset.save(commit=True)


admin.site.register(Content)
admin.site.register(UserAnswers)

