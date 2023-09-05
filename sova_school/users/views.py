from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model
from sova_school.users.forms import RegisterUserForm, LoginUserForm, UserEditForm, UserPasswordChangeForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import User
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Log the user in after registration
        login(request, user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id})
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


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
    def form_valid(self, form):
        result = super().get_context_data()
        save_changes = self.request.GET.get('save_changes')
        if save_changes:
            save_changes.save()
        return result


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


class PasswordChangeView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/profile_password_change.html'


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

        return HttpResponseRedirect(self.next_page)
