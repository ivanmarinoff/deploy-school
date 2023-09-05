from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from sova_school.global_content.views import ReadGlobalContentView, CreateContentView, EditGlobalContentView, \
    DeleteGlobalContentView, DetailGlobalContentView, GlobalContentListView

urlpatterns = [
                  path('read_content/', ReadGlobalContentView.as_view(), name='global-read-content'),
                  path('detail_content/<slug:slug>/', DetailGlobalContentView.as_view(), name='global-detail-content'),
                  path('create_content/', CreateContentView.as_view(), name='global-create-content'),
                  path('edit_content/<slug:slug>/', EditGlobalContentView.as_view(), name='global-edit-content'),
                  path('delete_content/<slug:slug>/', DeleteGlobalContentView.as_view(), name='global-delete-content'),
                  path('global_content/', GlobalContentListView.as_view(), name='api-global-content-list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
