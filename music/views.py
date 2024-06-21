from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Song, Album, Singer
from django.views.generic import CreateView, TemplateView
from .serializers import SongSerializer, AlbumSerializer, SingerSerializer
from .forms import SongForm, SingerForm, AlbumForm
from django.urls import reverse_lazy

def get_all_songs():
    songs = Song.objects.all().order_by('nombre')
    songs_serializers = SongSerializer(songs, many=True)
    return songs_serializers.data

def get_all_albums():
    albums = Album.objects.all().order_by('nombre')
    albums_serializers = AlbumSerializer(albums, many=True)
    return albums_serializers.data

def get_all_singers():
    singers = Singer.objects.all().order_by('nombre')
    singers_serializers = SingerSerializer(singers, many=True)
    return singers_serializers.data

def index(request):
    songs = Song.objects.all().order_by('nombre')
    singers = Singer.objects.all().order_by('nombre')
    albums = Album.objects.all().order_by('nombre')
    return render(request, 'index.html', {'songs': songs, 'albums': albums, 'singers': singers})

def songs_rest(request):
    songs = get_all_songs()
    return JsonResponse(songs, safe=False)

def singers_rest(request):
    singers = get_all_singers()
    return JsonResponse(singers, safe=False)

def albums_rest(request):
    albums = get_all_albums()
    return JsonResponse(albums, safe=False)

class CreateMusicView(TemplateView):
    template_name = 'create_music.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['song_form'] = SongForm()
        context['album_form'] = AlbumForm()
        context['singer_form'] = SingerForm()
        return context

def handle_form_submission(request, form_class, success_url):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class()
    return form

def create_song(request):
    song_form = handle_form_submission(request, SongForm, reverse_lazy('create_music'))
    return render(request, 'create_music.html', {'song_form': song_form, 'album_form': AlbumForm(), 'singer_form': SingerForm()})

def create_album(request):
    album_form = handle_form_submission(request, AlbumForm, reverse_lazy('create_music'))
    return render(request, 'create_music.html', {'song_form': SongForm(), 'album_form': album_form, 'singer_form': SingerForm()})

def create_singer(request):
    singer_form = handle_form_submission(request, SingerForm, reverse_lazy('create_music'))
    return render(request, 'create_music.html', {'song_form': SongForm(), 'album_form': AlbumForm(), 'singer_form': singer_form})
