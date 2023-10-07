# from django.contrib.auth import get_user_model
# from . import views
# from django.urls import path, include, reverse_lazy
# from sova_school.users.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileEditView, ProfileDeleteView, \
#     ProfileDetailsView, PasswordChangeView, PasswordChangeDoneView
#
# #
# UserModel = get_user_model()
# #
# urlpatterns = [
#     path('api/register/', views.register_user, name='api-register-user'),
#     path('api/login/', views.LoginApiUserView.as_view(), name='api-login-user'),
#     path('api/profile/', views.ProfileApiDetailsView.as_view(), name='api-profile-details'),
#
#     path('register/', RegisterUserView.as_view(success_url=reverse_lazy('register_user')), name='register_user'),
#     path('login/', LoginUserView.as_view(), name='login_user'),
#     path('logout/', LogoutUserView.as_view(), name='logout_user'),
#     path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
#
#     path('profile/<int:pk>/', include([
#         path('', ProfileDetailsView.as_view(), name='profile-details'),
#         path('edit/', ProfileEditView.as_view(), name='profile-edit'),
#         path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
#         path('password_change/', PasswordChangeView.as_view(
#             success_url=reverse_lazy('password_change_done')
#         ), name='password_change'),
#
#     ]))]

from django.contrib.auth import get_user_model
from django.urls import path, include, reverse_lazy, re_path

from sova_school.users.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileEditView, ProfileDeleteView, \
    ProfileDetailsView, PasswordChangeView, PasswordChangeDoneView


UserModel = get_user_model()

urlpatterns = [
    # re_path(r'^register_user/$', views.register_user, name='register-user'),
    # re_path(r'^login_user/$', views.LoginApiUserView.as_view(), name='login-user'),
    # re_path(r'^profile_user/$', views.ProfileApiDetailsView.as_view(), name='profile-details'),
    path('register/', RegisterUserView.as_view(success_url=reverse_lazy('register_user')), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
        path('password_change/', PasswordChangeView.as_view(
            success_url=reverse_lazy('password_change_done')
        ), name='password_change'),

    ]))]
