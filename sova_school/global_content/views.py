from django.core.files.storage import default_storage
from django.urls import reverse_lazy
from django.views import generic as views, generic
from sova_school.chat.mixins import CustomLoginRequiredMixin, ErrorRedirectMixin
from sova_school.global_content.forms import GlobalContentModelForm, GlobalContentEditForm, GlobalContentReadForm, \
    GlobalContentDeleteForm
from sova_school.global_content.models import Level_2


# class GlobalContentListView(generics.ListCreateAPIView):
#     queryset = GlobalContent.objects.all().order_by('-updated_at')
#     serializer_class = GlobalContentSerializer

class GlobalContentLiveStreamView(CustomLoginRequiredMixin, generic.TemplateView):
    template_name = '../rtmp/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





class CreateContentView(CustomLoginRequiredMixin, views.CreateView):
    template_name = "global_content/create_content.html"
    form_class = GlobalContentModelForm

    def get_success_url(self):
        return reverse_lazy('global-read-content')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Save the form data without saving the files in the database
        instance = form.save(commit=False)

        # Handle the video and photo files separately
        video_file = form.cleaned_data.get('video_file')
        document_file = form.cleaned_data.get('document_file')

        # Save the video file to a separate location
        if video_file:
            video_path = default_storage.save('videos/' + video_file.name, video_file)
            instance.video_file = video_path

        # Save the photo file to a separate location
        if document_file:
            document_path = default_storage.save('files/' + document_file.name, document_file)
            instance.document_file = document_path

        # Save the instance with the updated file paths
        instance.save()

        return super().form_valid(form)


class EditGlobalContentView(CustomLoginRequiredMixin, views.UpdateView):
    model = Level_2
    template_name = "global_content/edit_content.html"
    form_class = GlobalContentEditForm

    def get_success_url(self):
        return reverse_lazy('global-read-content')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().dispatch(request, *args, **kwargs)


class ReadGlobalContentView(CustomLoginRequiredMixin, views.ListView):
    model = Level_2
    template_name = 'global_content/read_content.html'
    form_class = GlobalContentReadForm
    success_url = reverse_lazy('global-read-content')
    paginate_by = 5
    context_object_name = 'global_content'
    object_list = Level_2.objects.all().order_by('title')

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class DetailGlobalContentView(ErrorRedirectMixin, views.DetailView):
    model = Level_2
    template_name = 'global_content/detail_content.html'

    def get_success_url(self):
        return reverse_lazy('global-read-content', kwargs={'slug': self.object.slug})


class DeleteGlobalContentView(CustomLoginRequiredMixin, views.DeleteView):
    model = Level_2
    template_name = 'global_content/delete_content.html'
    success_url = reverse_lazy('global-read-content')
    form_class = GlobalContentDeleteForm

    def get_form_kwargs(self):
        instance = self.get_object()
        form = super().get_form_kwargs()
        form.update(instance=instance)
        return form
