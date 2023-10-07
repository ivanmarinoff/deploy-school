from sova_school.content.forms import ContentModelForm, ContentDeleteForm, ContentEditForm
from sova_school.content.models import Content
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from rest_framework import generics
from .serializers import ContentSerializer
from ..chat.mixins import CustomLoginRequiredMixin, ErrorRedirectMixin


class ContentListView(CustomLoginRequiredMixin, auth_mixins.LoginRequiredMixin, generics.ListAPIView):
    queryset = Content.objects.all().order_by('-updated_at')
    serializer_class = ContentSerializer


class CreateContentView(CustomLoginRequiredMixin, auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Content
    template_name = "content/create_content.html"
    # fields = ['title', 'text']
    form_class = ContentModelForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'slug': self.object.slug})


class EditContentView(CustomLoginRequiredMixin, auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Content
    template_name = "content/edit_content.html"
    # fields = ['title', 'text', 'user_choices']

    form_class = ContentEditForm

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'slug': self.object.slug})


class ReadContentView(CustomLoginRequiredMixin, auth_mixins.LoginRequiredMixin, views.ListView):
    model = Content
    template_name = 'content/read_content.html'
    # form_class = ContentReadForm
    # success_url = reverse_lazy('read-content')
    paginate_by = 5
    context_object_name = 'content'
    object_list = Content.objects.all().order_by('title')

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter(text__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

    def get_form(self, *args, **kwargs):
        form = super().object_list(*args, **kwargs)
        # form.instance.user.pk = self.request.user

        return form

    def success_url(self):
        return reverse_lazy('read-content', kwargs={'pk': self.request.user.pk})


class DetailContentView(CustomLoginRequiredMixin, auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Content
    template_name = 'content/detail_content.html'
    context_object_name = 'content'

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'slug': self.object.slug})


class DeleteContentView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Content
    template_name = 'content/delete_content.html'
    # success_url = reverse_lazy('read-content')
    form_class = ContentDeleteForm

    def get_form_kwargs(self):
        instance = self.get_object()
        form = super().get_form_kwargs()
        form.update(instance=instance)
        return form

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'slug': self.object.slug})