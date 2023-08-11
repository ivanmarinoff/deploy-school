from django import forms
from django.forms import CheckboxInput
from sova_school.content.models import Content


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
#                 # field.widget.attrs['disabled'] = 'disabled'
#                 field.widget.attrs['readonly'] = 'readonly'


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
        # widget = forms.CheckboxSelectMultiple,
        # widgets = {
        #     'choices': CheckboxInput(attrs={'class': 'required checkbox form control'}),
        # }
        # widgets = {
        #     # 'title': forms.Textarea(attrs={'placeholder': 'Add title...'}),
        #     'text': forms.Textarea(attrs={'placeholder': 'Add content...'}),
        # }




class ContentEditForm(ContentModelForm):
    class Meta:
        model = Content
        # disabled_fields = ('title', 'text')
        exclude = ('user', 'slug', 'updated_at')
        fields = ['title', 'text', "image_url"]
        # widgets = {
        #     'title': forms.Textarea(attrs={'readonly': 'readonly'}),
        #     'text': forms.Textarea(attrs={'readonly': 'readonly'}),
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._disable_fields()




class ContentReadForm(ContentModelForm):
    class Meta:
        model = Content
        fields = ['title', 'text', "image_url"]



class ContentDeleteForm(ContentModelForm):
    # disabled_fields = '__all__'

    # def get_form(self, *args, **kwargs): # TODO diesabled fields
    #     form = super().get_form(*args, **kwargs)
    #     for field in self.disabled_fields:
    #         form.fields[field].widget.attrs['disabled'] = 'disabled'
    #     return form

    # fields = {'title': forms.TextInput(attrs={'disabled': 'disabled'}),
    #           'text': forms.Textarea(attrs={'disabled': 'disabled'})}

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._disable_fields()

    # def save(self, commit=True):
    #     if commit:
    #         self.instance.delete()
    #     return self.instance
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return super().save(*args, **kwargs)
