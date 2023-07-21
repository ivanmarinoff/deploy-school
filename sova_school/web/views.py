from django.contrib.auth import get_user_model
from django.views import generic as views


UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        pass


class SchoolProgramView(views.TemplateView):
    template_name = 'home/school_program.html'

    def get_context_data(self, **kwargs):
        pass