from rest_framework import serializers
from .models import Level_2


class GlobalContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level_2
        fields = '__all__'
