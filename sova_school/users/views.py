from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model, login
from sova_school.users.forms import RegisterUserForm, LoginUserForm, UserEditForm, UserPasswordChangeForm
from django.contrib.auth import authenticate

UserModel = get_user_model()

data_to_cache = {'key': 'value'}
cache.set('my_key', data_to_cache)

# Retrieve data from the cache
cached_data = cache.get('my_key')

if cached_data is None:
    # Data not in cache, fetch from database or perform calculation
    # and store it in cache
    cached_data = {'key': 'value'}
    cache.set('my_key', cached_data)


class OnlyAnonymousMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.getsuccess_url)
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        return self.success_url or reverse('login_user')


class RegisterUserView(OnlyAnonymousMixin, views.CreateView):
    model = UserModel
    template_name = 'home/signup.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_user')
    class_name = 'signup'

    def form_valid(self, form):
        valid = super(RegisterUserView, self).form_valid(form)
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

    def form_invalid(self, form):
        form.errors.clear()
        form.add_error(None, '   Invalid Email or Password')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class LoginUserView(auth_views.LoginView):
    form_class = LoginUserForm
    template_name = 'home/login.html'
    success_url = reverse_lazy('profile-details')
    class_name = 'login'
    redirect_authenticated_user = True

    def form_valid(self, form):
        result = form.cleaned_data.get('username')
        if not result:
            self.request.session.clear()
            self.request.session.set_expiry(0)

        return super().form_valid(form)

    def form_invalid(self, form):
        form.errors.clear()
        form.add_error(None, '   Invalid Username or Password')
        return super().form_invalid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})


class LogoutUserView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy('index')

    def get_next_page(self):
        next_page = self.request.GET.get('next')
        if next_page:
            return next_page
        return self.next_page

    def post(self, request, *args, **kwargs):
        # Perform any custom actions before logout, if needed
        # For example, saving user activity or updating user status

        # Call the parent class's post method to perform the logout
        response = super().post(request, *args, **kwargs)

        # Perform any additional actions after logout, if needed

        # Redirect to the next page after logout
        return HttpResponseRedirect(self.get_next_page())

    # def form_valid(self, form):
    #     result = super().get_context_data()
    #     save_changes = self.request.GET.get('save_changes')
    #     if save_changes:
    #         save_changes.save()
    #     return result


class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'users/profile-details.html'
    model = UserModel
    form_class = UserEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'users/profile-edit-page.html'
    model = UserModel
    form_class = UserEditForm

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        result = super().form_valid(form)
        save_changes = self.request.GET.get('save_changes')
        if save_changes:
            self.object.save()
        return result


class PasswordChangeView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/profile_password_change.html'


class PasswordChangeDoneView(auth_views.LogoutView):
    template_name = 'users/password_change_done.html'
    success_url = reverse_lazy('password_change_done')

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class ProfileDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'users/profile-delete-page.html'
    next_page = reverse_lazy('index')

    def post(self, *args, pk):
        self.request.user.delete()

        return HttpResponseRedirect(self.next_page)
