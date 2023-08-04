from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Content, UserAnswers
from django import forms


class role_inline(admin.TabularInline):
    model = Content
    extra = 1

#
# @admin.register(UserChoices)
# class UserChoicesAdmin(admin.ModelAdmin):
#     inlines = [role_inline]
#
#     fieldsets = [(None, {"fields": ["choices"]})]
#

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "user_choices", "created_at"]
    list_filter = ["user"]
    # search_fields = ['user_choices']
    fieldsets = [
        (None, {"fields": ["title", "text"]}),
        ("Permissions", {"fields": ["user", "user_choices"]}),
    ]

    choices = forms.ModelMultipleChoiceField(
        queryset=Content.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name="Choices",
            is_stacked=False
        )
    )

    def save_formset(self, request, form, formset, change):
        for object in formset.save():
            object.name = object.name.upper()
        formset.save(commit=True)

    def __str__(self) -> str:
        return f'{self.form}'


@admin.register(UserAnswers)
class UserAnswersAdmin(admin.ModelAdmin):
    # filter_horizontal = ["user_choices"]
    list_display = ["user"]
    list_filter = ["user"]
    fieldsets = [(None, {"fields": ["user","user_choices"]}),
                 ("Content", {'fields': ['updated']}), ]



    # class Meta:
    #     model = UserChoices
    #     fields = '__all__'
    #
    # def __init__(self, *args, **kwargs):
    #     super(UserAnswersAdmin, self).__init__(*args, **kwargs)
    #
    #     if self.instance and self.instance.pk:
    #         self.fields['choices'].initial = self.instance.choices.all()

    # def save(self, commit=True):
    #     content = super(UserAnswersAdmin, self).save(commit=False)
    #
    #     if commit:
    #         content.save()
    #
    #     if content.pk:
    #         content.choices = self.cleaned_data['choices']
    #         self.save_m2m()
    #
    #     return content
    def save(self, commit=True):
        new_content = super().save(commit=False)
        if commit:
            self.content = new_content
            new_content.save()

        return new_content
    # def save_formset(self, request, form, formset, change):
    #     for object in formset.save(): # Here
    #         object.name = object.name.upper()
    #     formset.save(commit=True)

# admin.site.register(Content)
# admin.site.register(UserAnswers)
