from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']

    def save_formset(self, request, form, formset, change):
        for object in formset.save():
            object.name = object.name.upper()
        formset.save(commit=True)
