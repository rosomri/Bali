from rest_framework import serializers
from playlist.models import Song, AccountSong, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title', 'image']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'artist', 'genre', 'title', 'image']