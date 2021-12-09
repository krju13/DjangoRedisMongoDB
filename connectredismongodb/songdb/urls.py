from django.urls import path
from .views import SongList
urlpatterns = [
    path('song/',SongList.as_view(),name="song"),
]