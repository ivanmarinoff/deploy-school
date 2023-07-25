from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model, login
from sova_school.users.forms import RegisterUserForm, LoginUserForm, UserEditForm

UserModel = get_user_model()


class OnlyAnonymousMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)


# Bear minimum on RegisterUserView!
class RegisterUserView(OnlyAnonymousMixin, views.CreateView):
    model = UserModel
    template_name = 'home/signup.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_user')
    class_name = 'signup'

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object

    def get_success_url(self):
        return ('login_user',)

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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    # def get_success_url(self):
    #     return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


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

    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        result = super().form_valid(form)
        save_changes = self.request.GET.get('save_changes')
        if save_changes:
            self.object.save()
        return result
    #
    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #     form.instance.user = self.request.user
    #     return form


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


# class UsersPasswordChangeView(auth_views.PasswordChangeView):
#     model = UserModel
#     template_name = 'users/profile_password_change.html'
#     success_url = reverse_lazy('users:password_change_done')
#
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = User.objects.filter(pk=self.kwargs['pk'])
#         return kwargs
#
#     def form_valid(self, form):
#         form.save()
#         del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
#         update_session_auth_hash(self.request, form.user)
#         return super().form_valid(form)


class PasswordChangeDoneView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    # form_class = PasswordChangeForm
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
