from django.urls import path
from sova_school.web import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('program/', views.SchoolProgramView.as_view(), name='school_program'),
]