from django.contrib.auth import views as auth_views
from django.urls import path, include, reverse_lazy
from sova_school.users.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileEditView, ProfileDeleteView, \
    ProfileDetailsView, PasswordChangeView, PasswordChangeDoneView

# app_name = 'users'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
        path('password_change/', PasswordChangeView.as_view(
            success_url=reverse_lazy('password_change_done')
        ), name='password_change'),
        path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    ]))]
