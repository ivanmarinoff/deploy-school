from sova_school.content.forms import ContentModelForm, ContentEditForm, ContentDeleteForm, ContentReadForm
from sova_school.content.models import Content
from django.urls import reverse_lazy
from django.views import generic as views


class CreateContentView(views.CreateView):
    model = Content
    template_name = "content/create_content.html"
    # fields = ['title', 'text']
    form_class = ContentModelForm

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'pk': self.object.pk})

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class EditContentView(views.UpdateView):
    model = Content
    template_name = "content/edit_content.html"
    # fields = ['title', 'text']
    form_class = ContentEditForm

    def get_success_url(self):
        return reverse_lazy('read-content', kwargs={'pk': self.object.pk})

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class ReadContentView(views.ListView):
    model = Content
    template_name = 'content/read_content.html'
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


# class ContentDetailsView(views.DetailView):
#     model = Content
#     template_name = 'content/content_details.html'
    # slug_field = Content.slug
    # pk_url_kwarg = 'id'

    # fields = ['text']

    # def get_success_url(self):
    #     return reverse_lazy('edit-content', kwargs={'pk': self.object.user.pk})
    #
    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #     form.instance.user = self.request.user
    #     return form
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['content'] = self.request.user.content_set.all()
    #     context['query'] = self.request.GET.get('query')
    #     return context


class DeleteContentView(views.DeleteView):
    model = Content
    template_name = 'content/delete_content.html'
    success_url = reverse_lazy('read-content')
    form_class = ContentDeleteForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form

# def create_content(request):
#     form = ContentModelForm()
#     if request.method == 'POST':
#         form = ContentModelForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             content = form.save(commit=False)
#             content.user = request.user
#             form.save()
#             return redirect('user-content')
#
#         context = {
#             'form': form,
#         }
#
#         return render(request, template_name='content/user_content.html', context=context)
#
#
# def show_content_details(request, username, slug):
#     slug = UserContent.objects.get(username=username, slug=slug)
#     all_content = UserContent.objects.all()
#     context = {
#         'content_title': slug,
#         'all_content': all_content,
#     }
#
#     return render(request, template_name='content/user_content.html', context=context)
#
#
# def delete_content(request, pk):
#     content = UserContent.object.get(pk=pk)
#     content.delete()
#     return redirect('index')
