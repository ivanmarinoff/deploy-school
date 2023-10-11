from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
from .models import Room
from ..settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def index_view(request):
    return redirect('room', room_name='general')
    # rooms = Room.objects.all()
    # return render(request, '../rtmp/index.html', {
    #     'rooms': rooms,
    # })


@login_required(login_url=LOGIN_URL)
def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, '../rtmp/index.html', {
        'room': chat_room,
    })


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
