from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # Inherits Attributes from User default instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # spotify uri, unique id for every user
    spotify_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=False)
    spotify_name = models.CharField(max_length=50, blank=True)
    deezer_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.CharField(max_length=50, blank=False, primary_key=True)
    name = models.TextField(max_length=100, blank=False)
    artist = models.TextField(max_length=100, blank=False)
    image_src = models.URLField()

    class Foo(models.Model):
        PLATFORM_CHOICES = (
            ('S', 'Spotify'),
            ('D', 'Deezer'),
        )
    platform = models.CharField(max_length=1, choices=Foo.PLATFORM_CHOICES, default='S')

    # TODO check if a song has one genre or multiple
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class ProfileSong(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class ProfileGenre(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

