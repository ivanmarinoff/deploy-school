from rest_framework import serializers
from .models import WEBContent


class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = WEBContent
        fields = '__all__'