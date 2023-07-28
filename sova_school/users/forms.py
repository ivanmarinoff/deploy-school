from django.contrib.auth import forms as auth_forms, get_user_model, update_session_auth_hash
from django import template
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect

register = template.Library()

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__clear_fields_helper_text()

        for field_name in ['username', 'email', 'password1', 'password2']:
            self.fields[field_name].help_text = None

    def __clear_fields_helper_text(self):
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs['class'] = 'form-control'



    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

        # def save(self, commit=True):
        #     user = super().save(commit=commit)
        #     profile = UserModel(
        #         user=user,
        #     )
        #     if commit:
        #         profile.save()
        #     return user


class LoginUserForm(auth_forms.AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')
        labels = {
            'username': 'Username',
            'password': 'Password',
        }


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'username': 'Username',
            'password': 'Password',
        }


class UserPasswordChangeForm(auth_forms.PasswordChangeForm):
    class Meta:
        model = UserModel

    def check_password(self):
        if self.cleaned_data['old_password'] == self.cleaned_data['new_password2']:
            return True
        else:
            return False

    # fields = ('old_password', 'new_password1', 'new_password2')
    # labels = {
    #     'old_password': 'Old Password',
    #     'new_password1': 'New Password',
    #     'new_password2': 'Confirm New Password',
    # }
    # widgets = {
    #     'old_password': forms.CharField(widget=forms.PasswordInput(
    #         attrs={'class': 'form-control', 'type': 'password', "placeholder": "Old Password"})
    #                                     ),
    #     'new_password1': forms.CharField(max_length=50, widget=forms.PasswordInput(
    #         attrs={'class': 'form-control', 'type': 'password', "placeholder": "New Password"})
    #                                       ),
    #     'new_password2': forms.CharField(max_length=50, widget=forms.PasswordInput(
    #         attrs={'class': 'form-control', 'type': 'password', "placeholder": "Confirm New Password"})
    #                                       )
    # }

    # def password_change(request):
    #     if request.method == "POST":
    #         form = PasswordChangeForm(user=request.user, data=request.POST)
    #         if form.is_valid():
    #             form.save()
    #             update_session_auth_hash(request, form.user)
    #             request.user.logout()
    #             return redirect('password_change_done')


@register.filter
def form_field_class(form_field, className):
    default_classname = form_field.field.widget.attrs.get('class', '')
    form_field.field.widget.attrs['class'] = default_classname + ' ' + className
    return form_field