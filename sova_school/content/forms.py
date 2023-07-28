from django import forms
from sova_school.content.models import Content


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
                # field.widget.attrs['readonly'] = 'readonly'


class ContentModelForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'text']
        widgets = {'text': forms.Textarea(attrs={'placeholder': 'Add content...'})}


# class SearchForm(forms.Form):
#     content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search content...'}))


class ContentEditForm(ContentModelForm):
    pass
    # disabled_fields = ('title',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._disable_fields()


class ContentReadForm(ContentModelForm):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._disable_fields()


class ContentDeleteForm(ContentModelForm):
    # disabled_fields = '__all__'



    # fields = {'title': forms.TextInput(attrs={'disabled': 'disabled'}),
    #           'text': forms.Textarea(attrs={'disabled': 'disabled'})}

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
