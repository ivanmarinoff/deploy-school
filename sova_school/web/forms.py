from django import forms
from django import template

from sova_school.web.models import WEBContent

register = template.Library()


class WEBContentForm(forms.ModelForm):
    class Meta:
        model = WEBContent
        fields = '__all__'


class WEBContentReadForm(WEBContentForm):
    pass


# class WEBContentDeleteForm(WEBContentForm):
#     def save(self, commit=True):
#         if commit:
#             self.instance.delete()
#         return self.instance

# @register.filter
# def form_field_class(form_field, className):
#     default_classname = form_field.field.widget.attrs.get('class', '')
#     form_field.field.widget.attrs['class'] = default_classname + ' ' + className
#     return form_field