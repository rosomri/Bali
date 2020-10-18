from django.contrib import admin
from playlist.models import AccountSong, Song, Genre

admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(AccountSong)
