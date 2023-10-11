from rest_framework import generics

from sova_school.content.forms import ContentModelForm, ContentDeleteForm, ContentEditForm, ContentReadForm
from sova_school.content.models import Level_1
from django.urls import reverse_lazy
from django.views import generic as views, generic

from .serializers import ContentSerializer
from ..chat.mixins import CustomLoginRequiredMixin, ErrorRedirectMixin
from django.core.files.storage import default_storage


class ContentListView(ErrorRedirectMixin, CustomLoginRequiredMixin, generics.ListAPIView):
    queryset = Level_1.objects.all().order_by('-updated_at')
    serializer_class = ContentSerializer


class ContentLiveStreamView(CustomLoginRequiredMixin, generic.TemplateView):
    template_name = '../rtmp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateContentView(CustomLoginRequiredMixin, views.CreateView):
    template_name = "content/create_content.html"
    form_class = ContentModelForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form

    def get_success_url(self):
        return reverse_lazy('read-content')

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


class EditContentView(CustomLoginRequiredMixin, views.UpdateView):
    model = Level_1
    template_name = "content/edit_content.html"
    form_class = ContentEditForm

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('read-content')


class ReadContentView(CustomLoginRequiredMixin, views.ListView):
    model = Level_1
    template_name = 'content/read_content.html'
    form_class = ContentReadForm
    success_url = reverse_lazy('read-content')
    paginate_by = 5
    context_object_name = 'content'
    object_list = Level_1.objects.all().order_by('title')

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter(text__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class DetailContentView(ErrorRedirectMixin, views.DetailView):
    model = Level_1
    template_name = 'content/detail_content.html'

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'slug': self.object.slug})


class DeleteContentView(CustomLoginRequiredMixin, views.DeleteView):
    model = Level_1
    template_name = 'content/delete_content.html'
    success_url = reverse_lazy('read-content')
    form_class = ContentDeleteForm

    def get_form_kwargs(self):
        instance = self.get_object()
        form = super().get_form_kwargs()
        form.update(instance=instance)
        return form
