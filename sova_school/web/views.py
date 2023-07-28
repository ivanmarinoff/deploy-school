from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from sova_school.web.forms import WEBContentReadForm, WEBContentForm, WEBContentDeleteForm
from sova_school.web.models import WEBContent
from django.contrib.auth import mixins as auth_mixins

UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        pass


class SchoolLevel_1View(views.TemplateView):
    model = WEBContent
    form_class = WEBContentForm

    template_name = 'home/school_program_level_1.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy('school_program_level_1')
class SchoolLevel_2View(views.TemplateView):
    model = WEBContent
    form_class = WEBContentForm

    template_name = 'home/school_program_level_2.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy('school_program_level_2')

class CreateWEBContentView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = WEBContent
    template_name = 'home/create_web_content.html'
    form_class = WEBContentForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form

    def get_success_url(self):
        return reverse_lazy('details_web_content', kwargs={'pk': self.object.pk})


class DetailWEBContentView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = WEBContent
    template_name = 'home/detail_web_content.html'
    # paginate_by = 5
    # context_object_name = 'WEBContent'
    form_class = WEBContentForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form

    def get_success_url(self):
        return reverse_lazy('read_web_content')


class ReadWEBContentView(views.ListView):
    model = WEBContent
    template_name = 'home/read_web_content.html'
    form_class = WEBContentReadForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form

    def get_success_url(self):
        return reverse_lazy('read_web_content')


class DeleteWEBContentView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = WEBContent
    template_name = 'home/delete_web_content.html'
    success_url = reverse_lazy('read_web_content')
    form_class = WEBContentDeleteForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form
