"""
URL configuration for sova_school project.

"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('sova_school.web.urls')),
    path('content/', include('sova_school.content.urls')),
    path('users/', include('sova_school.users.urls')),
    path('global_content/', include('sova_school.global_content.urls')),
    path('chat/', include('sova_school.chat.urls')),
    # path('api/', include('sova_school.content.urls')),
    # path('api/', include('sova_school.global_content.urls')),
    # path('api/', include('sova_school.users.urls')),
    # path('api/', include('sova_school.web.urls')),
]

if not settings.DEBUG:
    handler400 = 'sova_school.exception.bad_request'
    handler403 = 'sova_school.exception.permission_denied'
    handler500 = 'sova_school.exception.server_error'

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)