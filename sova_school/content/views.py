from django import forms
from django.http import Http404

from sova_school.content.forms import ContentModelForm, ContentDeleteForm, ContentEditForm
from sova_school.content.mixins.user_permition_mixin import UserRequiredMixin
from sova_school.content.models import Content, UserAnswers
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins


class CreateContentView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Content
    template_name = "content/create_content.html"
    # fields = ['title', 'text']
    form_class = ContentModelForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.content = self.object.save()
        return form

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'slug': self.object.slug})


class EditContentView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Content
    template_name = "content/edit_content.html"
    # fields = ['title', 'text', 'user_choices']

    form_class = ContentEditForm

    # success_url = reverse_lazy('read-content')

    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #     form.instance.user = self.request.user
    #     return form

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'slug': self.object.slug})

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(user=self.request.user)
    #     return queryset

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     if hasattr(self, "object"):
    #         kwargs.update({"instance": self.object})
    #     return kwargs

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     save_changes = self.request.POST.get('save_changes')
    #     if save_changes:
    #         self.object.save(commit=True)
    #     return result
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['contents'] = Content.objects.all() # TODO Changed...Content.objects.all()
    #     return context

    # def test_func(self):
    #     return self.get_object().user.pk == self.request.user.pk or self.request.user.is_superuser \
    #         or self.request.user.is_staff


    # def handle_no_permission(self):
    #     raise Http404()

    # def form_valid(self, form):
    #     self.object = form.save(commit=True)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)


class EditAnswerView(auth_mixins.LoginRequiredMixin, UserRequiredMixin, views.UpdateView):
    model = Content
    template_name = "content/edit_content.html"
    fields = ['title', 'text']
    # form_class = ContentEditForm
    success_url = reverse_lazy('read-content')

    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #     form.instance.user = self.request.user
    #     return form

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        self.object = form.save(commit=True)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ReadContentView(auth_mixins.LoginRequiredMixin, UserRequiredMixin, views.ListView):
    model = Content
    template_name = 'content/read_content.html'
    # form_class = ContentReadForm
    success_url = reverse_lazy('read-content')
    paginate_by = 5
    context_object_name = 'content'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter(text__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class DetailContentView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Content
    template_name = 'content/detail_content.html'


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

    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #     form.instance.user = self.request.user
    #     return form

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'slug': self.object.slug})


class UserAnswersView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = UserAnswers
    template_name = 'content/read_content.html'
    # form_class = ContentReadForm
    # success_url = reverse_lazy('read-content')

    # queryset = Content.objects.all()

    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #     form.instance.user = self.request.user
    #     form.save(commit=True)
    #     return form
    #
    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     save_changes = self.request.GET.get('save_changes')
    #     if save_changes:
    #         self.object.save(commit=True)
    #     return result

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'pk': self.object.pk})
