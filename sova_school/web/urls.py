from django.urls import path
from sova_school.web import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('program_level_1/', views.SchoolLevel_1View.as_view(), name='school_program_level_1'),
    path('program_level_2/', views.SchoolLevel_2View.as_view(), name='school_program_level_2'),
    path('create/<int:pk>/', views.CreateWEBContentView.as_view(), name='create_web_content'),
    path('read/', views.ReadWEBContentView.as_view(), name='read_web_content'),
    path('details/<int:pk>/', views.DetailWEBContentView.as_view(), name='details_web_content'),
    path('delete/', views.DeleteWEBContentView.as_view(), name='delete_web_content'),
]