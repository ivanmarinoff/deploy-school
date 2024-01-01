from django.urls import path, re_path
from sova_school.web import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  path('', views.IndexView.as_view(), name='home_page'),
                  path('program_level_1/', views.SchoolLevel_1View.as_view(), name='school_program_level_1'),
                  path('program_level_2/', views.SchoolLevel_2View.as_view(), name='school_program_level_2'),
                  path('read/', views.ReadWEBContentView.as_view(), name='read_web_content'),
                  path('bio_s_s/', views.BioWEBAutoSView.as_view(), name='bio_s_s'),
                  path('bio_e_s/', views.BioWEBAutoEView.as_view(), name='bio_e_s'),
                  path('bio_r_s/', views.BioWEBAutoRView.as_view(), name='bio_r_s'),
                  path('bio_m_r/', views.BioWEBAutoMView.as_view(), name='bio_m_r'),
                  re_path(r'^web/$', views.WEBListView.as_view({
                      'get': 'list',
                  })),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
