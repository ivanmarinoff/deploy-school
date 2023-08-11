from django import forms
from django.forms import CheckboxInput
from sova_school.content.models import Content


class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})


class ContentModelForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'text', "image_url"]


class ContentEditForm(ContentModelForm):
    class Meta:
        model = Content
        # disabled_fields = ('title', 'text')
        exclude = ('user', 'slug', 'updated_at')
        fields = ['title', 'text', "image_url"]


class ContentReadForm(ContentModelForm):
    class Meta:
        model = Content
        fields = ['title', 'text', "image_url"]


class ContentDeleteForm(ContentModelForm):

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return super().save(*args, **kwargs)
