import json
import re

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from .models import Room, Message
from ..users.models import User

UserModel = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_url = None
        self.room_name = None
        self.room_group_name = None
        self.room = None
        self.user = None
        # self.user_inbox = None

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']["room_name"]
        self.room_group_name = f'chat_{self.room_name}'
        self.room = Room.objects.get(name=self.room_name)
        self.user = self.scope['user']

        # Check if the room name is empty or contains invalid characters
        if not self.is_valid_room_name(self.room_name):
            self.close()
            return

        self.room = get_object_or_404(Room, name=self.room_name)
        self.user = self.scope['user']
        self.room.online.add(self.user)

        # connection has to be accepted
        self.room_url = reverse_lazy('room', kwargs={'room_name': self.room_name})
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        # send the user list to the newly joined user
        self.send(json.dumps({
            'type': 'user_list',
            'users': [user.username for user in self.room.online.all()],
        }))

        if self.user.is_authenticated:

            # send the join event to the room
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_join',
                    'user': self.user.username,
                }
            )
            self.room.online.add(self.user)

    def is_valid_room_name(self, room_name):
        # Define your validation logic here
        # For example, check if the room name is not empty and contains only alphanumeric characters
        return bool(room_name and re.match(r'^[a-zA-Z0-9]+$', room_name))


        # if self.user.is_staff:
        #     # Add other staff users to the room
        #     staff_users = User.objects.filter(groups__name='Staff')
        #     for staff_user in staff_users:
        #         self.room.online.add(staff_user)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

        if self.user.is_authenticated:

            # send the leave event to the room
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_leave',
                    'user': self.user.username,
                }
            )
            self.room.online.remove(self.user)

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if not self.user.is_authenticated:
            return
        # if message.startswith('/pm '):
        #     split = message.split(' ', 2)
        #     target = split[1]
        #     target_msg = split[2]
        #
        #     # send private message to the target
        #     async_to_sync(self.channel_layer.group_send)(
        #         f'inbox_{target}',
        #         {
        #             'type': 'private_message',
        #             'user': self.user.username,
        #             'message': target_msg,
        #         }
        #     )
        #     # send private message delivered to the user
        #     self.send(json.dumps({
        #         'type': 'private_message_delivered',
        #         'target': target,
        #         'message': target_msg,
        #     }))
        #     return

        # send chat message event to the room
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': self.user.username,
                'message': message,
            }
        )
        Message.objects.create(user=self.user, room=self.room, content=message)

    @classmethod
    def room_url(cls, room_name):
        return reverse("room", args=[room_name])

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))

    def user_join(self, event):
        self.send(text_data=json.dumps(event))

    def user_leave(self, event):
        self.send(text_data=json.dumps(event))

    # def private_message(self, event):
    #     self.send(text_data=json.dumps(event))
    #
    # def private_message_delivered(self, event):
    #     self.send(text_data=json.dumps(event))
