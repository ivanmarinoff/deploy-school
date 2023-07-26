from django.contrib.auth import views as auth_views, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model, login
from sova_school.users.forms import RegisterUserForm, LoginUserForm, UserEditForm

UserModel = get_user_model()


# class OnlyAnonymousMixin:
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(self.getsuccess_url)
#         return super().dispatch(self.request, *args, **kwargs)


# Bear minimum on RegisterUserView!
class RegisterUserView(views.CreateView):
    model = UserModel
    template_name = 'home/signup.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_user')
    class_name = 'signup'

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     login(self.request, self.object)
    #     return result

    def form_valid(self, form):
        valid = super(RegisterUserView, self).form_valid(form)
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)

        return valid

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['next'] = self.request.GET.get('next', '')
    #
    #     return context
    #
    # def get_success_url(self):
    #     return self.request.POST.get('next', self.success_url)


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
        form.add_error(None, 'Invalid Username or password')
        return super().form_invalid(form)



    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})


class LogoutUserView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    pass


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

    # fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        result = super().form_valid(form)
        save_changes = self.request.GET.get('save_changes')
        if save_changes:
            self.object.save()
        return result


class PasswordChangeView(auth_mixins.UserPassesTestMixin, auth_mixins.LoginRequiredMixin,
                         auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'users/profile_password_change.html'

    # def get_success_url(self):
    #     user_pk = self.kwargs['pk']
    #     return reverse_lazy('password_change_done', kwargs={'pk': user_pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.get_object()
        return context

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(UserModel, pk=pk)
        return obj

    def test_func(self):
        return self.get_object().pk == self.request.user.pk or self.request.user.is_superuser

    def handle_no_permission(self):
        raise Http404()


class PasswordChangeDoneView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
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
