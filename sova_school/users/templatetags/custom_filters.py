from django import template

from sova_school.content.models import Level_1

register = template.Library()


@register.filter
def placeholder(form_field, text):
    form_field.field.widget.attrs['placeholder'] = text
    return form_field


@register.filter
def form_field_class(form_field, className):
    default_classname = form_field.field.widget.attrs.get('class', '')
    form_field.field.widget.attrs['class'] = default_classname + ' ' + className
    return form_field


@register.filter
def sorting_filter():
    sorting = Level_1.objects.filter().order_by('-created_at')
    return sorting


@register.filter
def choices(user_choices):
    if user_choices is None:
        return ""
    return user_choices
