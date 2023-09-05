import os

from django.urls import reverse_lazy
from django.views import generic as views
from sova_school.global_content.forms import GlobalContentModelForm, GlobalContentEditForm, GlobalContentReadForm, \
    GlobalContentDeleteForm
from sova_school.global_content.models import GlobalContent
from rest_framework import generics
from .serializers import GlobalContentSerializer


class GlobalContentListView(generics.ListCreateAPIView):
    queryset = GlobalContent.objects.all().order_by('-updated_at')
    serializer_class = GlobalContentSerializer


class CreateContentView(views.CreateView):
    template_name = "global_content/create_content.html"
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
    form_class = GlobalContentEditForm

    def get_success_url(self):
        return reverse_lazy('global-read-content')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().dispatch(request, *args, **kwargs)


class ReadGlobalContentView(views.ListView):
    model = GlobalContent
    template_name = 'global_content/read_content.html'
    form_class = GlobalContentReadForm
    success_url = reverse_lazy('global-read-content')
    paginate_by = 5
    context_object_name = 'global_content'
    object_list = GlobalContent.objects.all().order_by('title')

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class DetailGlobalContentView(views.DetailView):
    model = GlobalContent
    template_name = 'global_content/detail_content.html'

    def get_success_url(self):
        return reverse_lazy('global-read-content', kwargs={'slug': self.object.slug})


class DeleteGlobalContentView(views.DeleteView):
    model = GlobalContent
    template_name = 'global_content/delete_content.html'
    success_url = reverse_lazy('global-read-content')
    form_class = GlobalContentDeleteForm

    def get_form_kwargs(self):
        instance = self.get_object()
        form = super().get_form_kwargs()
        form.update(instance=instance)
        return form
