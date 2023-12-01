from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'name', 'author', 'url', 'published_date']
