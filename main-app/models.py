# from django.db import models
# from django.contrib.auth.models import User
#
#
# class Profile(models.Model):
#     # Inherits Attributes from User default instance
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # spotify uri, unique id for every user
#     spotify_id = models.CharField(max_length=50, blank=False)
#
#     def __str__(self):
#         return self.user.username
#
#
# class Genre(models.Model):
#     name = models.CharField(max_length=50, blank=False)
#
#     def __str__(self):
#         return self.name
#
#
# class Song(models.Model):
#     id = models.CharField(max_length=50, blank=False, primary_key=True)
#     name = models.TextField(max_length=100, blank=False)
#     artist = models.TextField(max_length=100, blank=False)
#     image_src = models.URLField()
#     # TODO check if a song has one genre or multiple
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.id
#
#
# class ProfileSong(models.Model):
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     song = models.ForeignKey(Song, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0)
#
#
