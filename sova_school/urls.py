"""
URL configuration for sova_school project.

"""
from django.contrib import admin
from django.urls import path, include

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
