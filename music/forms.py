from django import forms

from .models import Song, Album, Singer


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = [
            'nombre',
            'album',
        ]

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'nombre',
            'singer',
        ]

class SingerForm(forms.ModelForm):
    class Meta:
        model = Singer
        fields = [
            'nombre',
        ]

