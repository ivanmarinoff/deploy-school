import os

from django.urls import reverse_lazy
from django.views import generic as views
from sova_school.global_content.forms import GlobalContentModelForm, GlobalContentEditForm, GlobalContentReadForm, \
    GlobalContentDeleteForm
from sova_school.global_content.models import GlobalContent


class CreateContentView(views.CreateView):
    # model = GlobalContent
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

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().get(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().post(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().dispatch(request, *args, **kwargs)

    # def get_form_kwargs(self):
    #     instance = self.get_object()
    #     form = super().get_form_kwargs()
    #     form.update(instance=instance)
    #     return form

    # def form_valid(self, form):
    #     self.object = form.save(commit=True)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)



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
    # photos = GlobalContent.objects.all()

    # def get_photos(self):
    #     self.photos = GlobalContent.objects.all()
    #     if self.object.photos is None:
    #         return self.object.photos
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['photos'] = self.get_photos()
    #     return context

    def get_success_url(self):
        return reverse_lazy('global-read-content', kwargs={'slug': self.object.slug})

    # def get_form(self, *args, **kwargs):
    #     form = super().get_object(*args, **kwargs)
    #     form.instance.user = self.request.user
    #     return form


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

    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #     form.instance.user = self.request.user
    #     return form
