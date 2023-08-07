from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email']

    permissions = forms.ModelMultipleChoiceField(
        queryset=UserModel.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name="Add permissions",
            is_stacked=False
        )
    )

    def save_formset(self, request, form, formset, change):
        for object in formset.save():
            object.name = object.name.upper()
        formset.save(commit=True)
