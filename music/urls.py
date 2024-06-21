from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index_music'),
    path('song_rest/', views.songs_rest, name='song_rest'),
    path('album_rest/', views.albums_rest, name='album_rest'),
    path('singer_rest/', views.singers_rest, name='singer_rest'),
    path('create_music/', views.CreateMusicView.as_view(), name='create_music'),
    path('new_music/', views.create_song, name='new_music'),
    path('new_album/', views.create_album, name='new_album'),
    path('new_singer/', views.create_singer, name='new_singer'),
]
