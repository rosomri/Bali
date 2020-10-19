from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


def upload_genre_location(instance, filename):
    file_path = 'genre/{title}-{filename}'.format(title=str(instance.title), filename=filename)
    return file_path


class Genre(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to=upload_genre_location, null=True, blank=True)

    def __str__(self):
        return self.title


def upload_song_location(instance, filename):
    file_path = 'song/{id}/{title}-{filename}'.format(id=str(instance.id), title=str(instance.title), filename=filename)
    return file_path


class Song(models.Model):
    id = models.CharField(max_length=50, blank=False, primary_key=True)
    title = models.TextField(max_length=10, blank=False)
    artist = models.TextField(max_length=100, blank=False)
    image = models.ImageField(upload_to=upload_song_location, null=True, blank=True)
    # TODO check if a song has one genre or multiple
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        unique_together = ('title', 'artist')


@receiver(post_delete, sender=Song)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class AccountSong(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ('account', 'song')


class AccountGenre(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('account', 'genre')