from django.shortcuts import render
from .models import Profile, Song, ProfileSong, Genre


def index(request):
    return render(request, 'index.html')
