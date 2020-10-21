from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from playlist.models import Song, AccountSong, Genre, AccountGenre
from account.models import Account
from playlist.api.serializers import GenreSerializer, SongSerializer, AccountGenreSerializer, AccountSongsSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


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
@permission_classes((IsAdminUser,))
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
@permission_classes((IsAdminUser,))
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
@permission_classes((IsAdminUser,))
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


# Reset user Songs and Genres
@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
def delete_song_view(request):
    request.user.pk



#   1) list: https://<your-domain>/api/playlist/account_song
#   2) pagination: http://<your-domain>/api/playlist/account_song?page=2
#   3) search: http://<your-domain>/api/playlist/account_song?search=<username>
#   For Admin Only
class ApiAccountSongListView(ListAPIView):
    queryset = AccountSong.objects.filter()
    serializer_class = AccountSongsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('=account__username',)


# GET all genres
class ApiGenreListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination


# GET all account genres for authenticated user
#   1) list: https://<your-domain>/api/playlist/account_genre/list
#   2) pagination: http://<your-domain>/api/playlist/account_song?page=2
class ApiAccountGenreListView(ListAPIView):
    serializer_class = AccountGenreSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        return AccountGenre.objects.filter(account__email=user)


# GET all songs (by account genres)
#   1) list: https://<your-domain>/api/playlist/optional_songs/<username>/
class ApiOptionalSongList(ListAPIView):
    serializer_class = SongSerializer
    pagination_class = PageNumberPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def get_queryset(self):
        genres = AccountGenre.objects.filter(account__username=self.kwargs['username'])
        return Song.objects.filter(genre__in=genres.values('genre'))


# DELETE all account genres
# POST liked genres
# POST liked songs
# GET whatsapp link
# POST create playlist


