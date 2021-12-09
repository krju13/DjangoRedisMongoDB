from .models import Song

def get_song():
    return list(Song.objects.prefetch_related('song'))