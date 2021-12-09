from rest_framework import serializers
from django.db.models import fields
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'