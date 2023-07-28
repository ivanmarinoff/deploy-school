from sova_school.web.models import WEBContent
from django import forms
from django import template

register = template.Library()


class WEBContentForm(forms.ModelForm):
    class Meta:
        model = WEBContent
        fields = ('title', 'text', 'image')


class WEBContentReadForm(WEBContentForm):
    pass


class WEBContentDeleteForm(WEBContentForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

@register.filter
def form_field_class(form_field, className):
    default_classname = form_field.field.widget.attrs.get('class', '')
    form_field.field.widget.attrs['class'] = default_classname + ' ' + className
    return form_field