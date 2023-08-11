import os

from django import forms

from sova_school.global_content.models import GlobalContent


class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})


class GlobalContentModelForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = GlobalContent
        fields = ['title', 'text', 'image_url', 'photos', 'slug']
        ordering = ['-created_at']


class GlobalContentEditForm(GlobalContentModelForm):
    pass


class GlobalContentReadForm(GlobalContentModelForm):
    pass


class GlobalContentDeleteForm(GlobalContentModelForm):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return super().save(*args, **kwargs)
