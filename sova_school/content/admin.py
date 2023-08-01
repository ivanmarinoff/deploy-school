from django.contrib import admin
from .models import Content, UserAnswers


class ContentAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "user_choices", "created_at", "updated_at"]

class UserAnswersAdmin(admin.ModelAdmin):
    list_display = ["user", "content", "updated"]


admin.site.register(Content)
admin.site.register(UserAnswers)

