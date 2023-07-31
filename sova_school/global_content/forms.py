from django import forms

from sova_school.global_content.models import GlobalContent


# class DisabledFormMixin:
#     disabled_fields = ()
#     fields = {}
#
#     def _disable_fields(self):
#         if self.disabled_fields == '__all__':
#             fields = self.fields.keys()
#         else:
#             fields = self.disabled_fields
#
#         for field_name in fields:
#             if field_name in self.fields:
#                 field = self.fields[field_name]
#                 field.widget.attrs['disabled'] = 'disabled'

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



# class GlobalSearchForm(forms.Form):
#     content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search content...'}))


class GlobalContentEditForm(GlobalContentModelForm):
    pass


class GlobalContentReadForm(GlobalContentModelForm):
    pass


class GlobalContentDeleteForm(GlobalContentModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
