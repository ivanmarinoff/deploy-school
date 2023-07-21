from django.urls import path, include

from sova_school.content.views import ReadContentView, CreateContentView, EditContentView, DeleteContentView

urlpatterns = (
    path('read_content/<int:pk>/', ReadContentView.as_view(), name='read-content'),
    path('create_content/<int:pk>/', CreateContentView.as_view(), name='create-content'),
    path('edit_content/<int:pk>/', EditContentView.as_view(), name='edit-content'),
    path('delete_content/<int:pk>/', DeleteContentView.as_view(), name='delete-content'),
)
