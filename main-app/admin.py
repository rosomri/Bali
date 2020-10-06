from django.contrib import admin
from .models import Profile, Song, ProfileSong, Genre, ProfileGenre


admin.site.register(Profile)
admin.site.register(Song)
admin.site.register(ProfileSong)
admin.site.register(Genre)
admin.site.register(ProfileGenre)

