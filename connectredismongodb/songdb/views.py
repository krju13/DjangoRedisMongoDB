from .models import Song
from .serializers import SongSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.cache import cache

class SongList(APIView):
    def get(self, request, format=None):
        song = cache.get_or_set('song',Song.objects.all())
        songSerializer = SongSerializer(song, many=True)
        return Response(songSerializer.data)
    def post(self, request,format=None):
        songSerializer = SongSerializer(data=request.data)
        if songSerializer.is_valid():
            cache.delete('song')
            songSerializer.save()
            return Response(songSerializer.data, status=status.HTTP_201_CREATED)
        return Response(songSerializer.errors, status=400)
