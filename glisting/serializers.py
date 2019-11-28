from rest_framework import serializers
from . import models


class GamesListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'platform', 'score', 'genre', 'editors_choice',)
        model = models.GamesList