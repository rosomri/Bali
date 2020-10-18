from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from playlist.models import Song, AccountSong, Genre
from account.models import Account
from playlist.api.serializers import GenreSerializer, SongSerializer
from rest_framework.generics import ListAPIView


# Get a specific genre details by title
@api_view(['GET'])
def detail_genre_view(request, title):
    try:
        genre = Genre.objects.get(title=title)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)


# Get a specific song details by id
@api_view(['POST'])
def create_song_view(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get a specific song details by id
@api_view(['GET'])
def detail_song_view(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SongSerializer(song)
    return Response(serializer.data)


# update a specific song details by id
@api_view(['PUT'])
def update_song_view(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = SongSerializer(song, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delete a specific song details by id
@api_view(['DELETE'])
def delete_song_view(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = song.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failure"
        return Response(data=data)
