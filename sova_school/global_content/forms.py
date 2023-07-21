from django import forms

from sova_school.global_content.models import GlobalContent


class DisabledFormMixin:
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget.attrs['disabled'] = 'disabled'


class ContentModelForm(forms.ModelForm):
    class Meta:
        model = GlobalContent
        fields = ['title', 'text', 'image_url', 'slug']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add content...'}),
            'title': forms.TextInput(attrs={'placeholder': 'Add title...'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Add image url...'}),
        }


class SearchForm(forms.Form):
    content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search content...'}))


class ContentEditForm(ContentModelForm):
    pass


class ContentReadForm(ContentModelForm):
    pass


class ContentDeleteForm(ContentModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
