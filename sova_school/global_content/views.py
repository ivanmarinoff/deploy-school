from django.urls import reverse_lazy
from django.views import generic as views
from sova_school.global_content.forms import GlobalContentModelForm, GlobalContentEditForm, GlobalContentReadForm,\
    GlobalContentDeleteForm
from sova_school.global_content.models import GlobalContent


class CreateContentView(views.CreateView):
    model = GlobalContent
    template_name = "global_content/create_content.html"
    # fields = ['title', 'text']
    form_class = GlobalContentModelForm

    def get_success_url(self):
        return reverse_lazy('global-read-content')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class EditGlobalContentView(views.UpdateView):
    model = GlobalContent
    template_name = "global_content/edit_content.html"
    # fields = ['title', 'text']
    form_class = GlobalContentEditForm

    def get_success_url(self):
        return reverse_lazy('global-read-content')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class ReadGlobalContentView(views.ListView):
    model = GlobalContent
    template_name = 'global_content/read_content.html'
    form_class = GlobalContentReadForm
    success_url = reverse_lazy('global-read-content')
    paginate_by = 5
    context_object_name = 'content'

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')

        queryset = queryset.filter(
            title__icontains=search
        )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class DetailGlobalContentView(views.DetailView):
    model = GlobalContent
    template_name = 'global_content/detail_content.html'

    def get_success_url(self):
        return reverse_lazy('global-read-content', kwargs={'pk': self.object.slug})

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class DeleteGlobalContentView(views.DeleteView):
    model = GlobalContent
    template_name = 'global_content/delete_content.html'
    success_url = reverse_lazy('global-read-content')
    form_class = GlobalContentDeleteForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form
