from django import forms
from django.forms import CheckboxInput
from sova_school.content.models import Content, UserAnswers


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
                # field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'


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
        fields = ['title', 'text', 'user_choices']
        # widget = forms.CheckboxSelectMultiple,
        widgets = {
            'choices': CheckboxInput(attrs={'class': 'required checkbox form control'}),
        }
        # widgets = {
        #     # 'title': forms.Textarea(attrs={'placeholder': 'Add title...'}),
        #     'text': forms.Textarea(attrs={'placeholder': 'Add content...'}),
        # }


# class SearchForm(forms.Form):
#     content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search content...'}))
# class ContentAnswerChoiceForm(forms.ModelForm):
#     class Meta:
#         model = UserAnswers
#         fields = ['user_choices']
#         # widgets = {
#         #     'answer': CheckboxInput(attrs={'class': 'required checkbox form control'}),
#         # }
#
#     def save(self, commit=True):
#         if commit:
#             self.instance.save()
#         return self.instance


# class ContentAnswerForm(ContentModelForm):
#     class Meta:
#         model = UserAnswers
#         fields = ['user']
        # widgets = {
        #     'answer': CheckboxInput(attrs={'class': 'required checkbox form control'}),
        # }

    # disabled_fields = ('title', 'text')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._disable_fields()
    #
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     return super().save(*args, **kwargs)

    # def save(self, commit=True):
    #     new_instance = super().save(commit=False)
    #     if commit:
    #         self.instance = new_instance
    #         new_instance.save()
    #         self.save_m2m()
    #         # self.instance.choices = self.cleaned_data['choices']
    #         # return new_instance
    #     return new_instance

    # def __str__(self):
    #     form = self.instance
    #     return form.__str__()


class ContentEditForm(DisabledFormMixin, ContentModelForm):
    class Meta:
        model = Content
        disabled_fields = ('title', 'text')
        exclude = ('user', 'slug', 'updated_at', 'user_choices',)
        # fields = ['title', 'text', 'user_choices']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return super().save(*args, **kwargs)


    def __str__(self):
        form = self.instance
        return form.__str__()

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     return super().save(*args, **kwargs)
    #
    # def __str__(self):
    #     return f'{self.title}'

    # def save(self, commit=True):
    #     if commit:
    #         self.instance.save()
    #     return self.instance


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

    # def save(self, commit=True):
    #     if commit:
    #         self.instance.delete()
    #     return self.instance
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return super().save(*args, **kwargs)
