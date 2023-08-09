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
class ContentAdminForm(admin.ModelAdmin):
    # readonly_fields = ('title', 'text')
    list_display = ["title", "text", "user_choices", "created_at", "slug"]
    list_filter = ["title"]
    # search_fields = ['user_choices']
    fieldsets = [
        (None, {"fields": ["title", "text"]}),
        ("Permissions", {"fields": ["slug", "user_choices"]}),
    ]

    choices = forms.ModelMultipleChoiceField(
        queryset=UserAnswers.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name="Choices",
            is_stacked=False
        )
    )

    class Meta:
        model = Content
        fields = '__all__'


    def save_formset(self, request, form, formset, change):
        for object in formset.save():
            object.name = object.name.upper()
        formset.save(commit=True)

    def __str__(self) -> str:
        return f'{self.form}'


class UserAnswersAdminForm(forms.ModelForm):
    # choices = forms.MultipleChoiceField(
    #     # queryset=Content.objects.all(),
    #     required=False,
    #     widget=FilteredSelectMultiple(
    #         verbose_name='choices',
    #         is_stacked=False
    #     )
    # )

    # filter_horizontal = ["user_choices"]
    list_display = ["user", "choices"]
    list_filter = ["user"]
    fieldsets = [(None, {"fields": ["user", "choices"]}),
                 ("Content", {'fields': ['updated']}), ]


    class Meta:
        model = Content
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(UserAnswersAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['choices'].initial = self.instance.choices.all()


    def save(self, commit=True):
        choice = super(UserAnswersAdminForm, self).save(commit=False)

        if commit:
            choice.save()

        if choice.pk:
            choice.content = self.cleaned_data['choices']
            self.save_m2m()

        return choice


class UserAnswersAdmin(admin.ModelAdmin):
    form = UserAnswersAdminForm
    list_display = ['user', 'updated']


class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm
    list_display = ['title', 'user', 'user_choices', 'created_at']

    # def save(self, commit=True):
    #
    #     new_content = super().save(commit=False)
    #     if commit:
    #         self.content = new_content
    #         new_content.save()
    #
    #     return new_content
    # def save_formset(self, request, form, formset, change):
    #     for object in formset.save(): # Here
    #         object.name = object.name.upper()
    #     formset.save(commit=True)


# admin.site.register(Content)
admin.site.register(UserAnswers, UserAnswersAdmin)

