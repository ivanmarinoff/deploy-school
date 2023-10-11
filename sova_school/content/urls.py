from django.conf import settings
from django.conf.urls.static import static

from sova_school.content.views import ReadContentView, CreateContentView, EditContentView, DeleteContentView, \
    DetailContentView, ContentLiveStreamView, ContentListView
from django.urls import path


urlpatterns = [
    path('read_content/', ReadContentView.as_view(), name='read-content'),
    path('live_stream/', ContentLiveStreamView.as_view(), name='live-stream'),
    path('detail_content/<slug:slug>/', DetailContentView.as_view(), name='detail-content'),
    path('create_content/', CreateContentView.as_view(), name='create-content'),
    path('edit_content/<slug:slug>/', EditContentView.as_view(), name='edit-content'),
    path('delete_content/<slug:slug>/', DeleteContentView.as_view(), name='delete-content'),
    path('content/', ContentListView.as_view(), name='api-content-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


