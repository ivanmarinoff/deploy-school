from django.urls import path, include

from sova_school.global_content.views import ReadContentView, CreateContentView, EditContentView, DeleteContentView

urlpatterns = (
    path('read_content/', ReadContentView.as_view(), name='global-read-content'),
    path('create_content/', CreateContentView.as_view(), name='global-create-content'),
    path('edit_content/', EditContentView.as_view(), name='global-edit-content'),
    path('delete_content/', DeleteContentView.as_view(), name='global-delete-content'),
)
