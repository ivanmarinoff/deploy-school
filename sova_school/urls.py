"""
URL configuration for sova_school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('sova_school.web.urls')),
    path('content/', include('sova_school.content.urls')),
    path('users/', include('sova_school.users.urls')),
    path('global_content/', include('sova_school.global_content.urls')),
    path('api/', include('sova_school.content.urls')),
    path('api/', include('sova_school.global_content.urls')),
    path('api/', include('sova_school.users.urls')),
    path('api/', include('sova_school.web.urls')),
]
