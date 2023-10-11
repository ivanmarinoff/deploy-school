from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path("<str:room_name>/", views.room_view, name='room'),
    path('rooms/', views.RoomListAPIView.as_view(), name='room-list'),
    path('messages/', views.MessageListAPIView.as_view(), name='message-list'),
]
