from rest_framework import serializers
from .models import GlobalContent


class GlobalContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalContent
        fields = '__all__'
