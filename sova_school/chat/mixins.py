from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.shortcuts import redirect, render

from sova_school.settings import LOGIN_URL

UserModel = get_user_model()


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = LOGIN_URL  # Replace with your actual login URL

    def handle_no_permission(self):
        return redirect(self.login_url)


class ErrorRedirectMixin(AccessMixin):

    def __init__(self):
        self.request = None

    # def Http404(self, request, *args, **kwargs):
    #     response = render(request, '../templates/errors/404_not_found.html')
    #     response.status_code = 404
    #     return response
    #
    # def Http500(self, request, *args, **kwargs):
    #     response = render(request, '../templates/errors/500_server_error.html')
    #     response.status_code = 500
    #     return response

    def handle_no_permission(self):
        return render(
            self.request, "../templates/errors/404_not_found.html",
            {'error_message': self.get_permission_denied_message()}
        )
    # def dispatch(self, request, error_message):
    #     return render(request, "../templates/errors/404_not_found.html", {'error_message': error_message})
