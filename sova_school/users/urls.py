from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include, reverse_lazy
from sova_school.users.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileEditView, ProfileDeleteView, \
    ProfileDetailsView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
        path('password_change/', PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password-change'),

    ]))]
