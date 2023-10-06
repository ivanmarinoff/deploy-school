from django.shortcuts import render, redirect

from .models import Room


def index_view(request):
    return redirect('room', room_name='general')
    # rooms = Room.objects.all()
    # return render(request, '../rtmp/index.html', {
    #     'rooms': rooms,
    # })


def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, '../rtmp/index.html', {
        'room': chat_room,
    })