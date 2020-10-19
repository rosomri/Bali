from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from playlist.models import Song, AccountSong, Genre, AccountGenre
from account.models import Account
from playlist.api.serializers import GenreSerializer, SongSerializer, AccountGenreSerializer
from rest_framework.generics import ListAPIView


# create a specific genre details by title
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_account_genre_view(request):
    title = request.data.get('title', '0')
    try:
        genre = Genre.objects.get(title=title)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    data['genre'] = genre.pk
    data['account'] = request.user.pk
    serializer = AccountGenreSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get a specific genre details by title
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def detail_genre_view(request):
    title = request.data.get('title', '0')
    try:
        genre = Genre.objects.get(title=title)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)


# post a new song
@api_view(['POST'])
#admin
def create_song_view(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get a specific song details by id
@api_view(['GET'])
def detail_song_view(request):
    id = request.data.get('id', '0')
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SongSerializer(song)
    return Response(serializer.data)


# update a specific song details by id
@api_view(['PUT'])
#admin
def update_song_view(request):
    id = request.data.get('id', '0')
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
#admin
def delete_song_view(request):
    id = request.data.get('id', '0')
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


# GET all genres
# GET all account genres
# DELETE all account genres
# GET all songs (by account genres)
# POST liked genres
# POST liked songs
# GET whatsapp link
# POST create playlist


