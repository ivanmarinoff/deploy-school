from sova_school.content.forms import ContentModelForm, ContentEditForm, ContentDeleteForm, ContentReadForm
from django.urls import reverse_lazy
from django.views import generic as views
from sova_school.global_content.models import GlobalContent


class CreateContentView(views.CreateView):
    model = GlobalContent
    template_name = "global_content/create_content.html"
    # fields = ['title', 'text']
    form_class = ContentModelForm

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'pk': self.object.pk})

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class EditContentView(views.UpdateView):
    model = GlobalContent
    template_name = "global_content/edit_content.html"
    # fields = ['title', 'text']
    form_class = ContentEditForm

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'pk': self.object.pk})

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class ReadContentView(views.ListView):
    model = GlobalContent
    template_name = 'global_content/read_content.html'
    form_class = ContentReadForm
    success_url = reverse_lazy('read-content')
    paginate_by = 1
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




class DeleteContentView(views.DeleteView):
    model = GlobalContent
    template_name = 'global_content/delete_content.html'
    success_url = reverse_lazy('read-content')
    form_class = ContentDeleteForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


