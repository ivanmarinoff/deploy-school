from django.contrib.auth import views as auth_views, login, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from sova_school.users.forms import RegisterUserForm, LoginUserForm, UserPasswordChangeForm
from sova_school.users.models import User

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

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    form_class = LoginUserForm
    template_name = 'home/login.html'
    success_url = reverse_lazy('profile-details')
    class_name = 'login'


class LogoutUserView(auth_views.LogoutView):
    pass
    # # next_page = reverse_lazy('index')
    # def get_success_url(self):
    #     return reverse_lazy('index')


class ProfileDetailsView(views.DetailView):
    template_name = 'users/profile-details.html'
    model = UserModel

    # user = User.objects.get(username=self.request.username)
    # user.set_password('new password')
    # user.save()

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileEditView(views.UpdateView):
    template_name = 'users/profile-edit-page.html'
    model = UserModel
    # form_class = UserEditForm
    fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PasswordChangeView(auth_views.PasswordChangeView):
    model = UserPasswordChangeForm
    template_name = 'users/profile_password_change.html'
    success_url = reverse_lazy('login_user')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = User.objects.filter(pk=self.kwargs['pk'])
        return kwargs

    # def change_password(request):
    #     if request.method == 'POST':
    #         form = PasswordChangeForm(request.user, request.POST)
    #         if form.is_valid():
    #             user = form.save()
    #             update_session_auth_hash(request, user)  # Important!
    #             return redirect('profile-details')
    #
    #     else:
    #         form = PasswordChangeForm(request.user)
    #     return render(request, 'users/profile-edit-page.html', {
    #         'form': form
    #     })

    # def update(self, instance, validated_data):
    #     user = self.context['request'].user
    #
    #     if user.pk != instance.pk:
    #         raise ValidationError({"authorize": "You dont have permission for this user."})
    #
    #     instance.first_name = validated_data['first_name']
    #     instance.last_name = validated_data['last_name']
    #     instance.email = validated_data['email']
    #     instance.username = validated_data['username']
    #     instance.set_password(validated_data['password'])
    #     instance.save()
    #
    #     instance.save()
    #
    #     return instance


class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'users/profile-delete-page.html'
    next_page = reverse_lazy('index')

    def post(self, *args, pk):
        self.request.user.delete()
