from rest_framework import serializers
from playlist.models import Song, AccountSong, Genre, AccountGenre


class AccountGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountGenre
        fields = ['account', 'genre']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title', 'image']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'artist', 'genre', 'title', 'image']


class AccountSongsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_account')
    song_title = serializers.SerializerMethodField('get_song_title')
    song_id = serializers.SerializerMethodField('get_song_id')

    class Meta:
        model = AccountSong
        fields = ['username', 'song', 'song_id', 'song_title', 'rating']

    def get_username_from_account(self, account_song):
        username = account_song.account.username
        return username

    def get_song_title(self, account_song):
        title = account_song.song.title
        return title

    def get_song_id(self, account_song):
        id = account_song.song.id
        return id