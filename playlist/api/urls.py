from django.urls import path
from playlist.api.views import (
    detail_genre_view,
    detail_song_view,
    delete_song_view,
    update_song_view,
    create_song_view,
    create_account_genre_view,
)
app_name = "playlist"

urlpatterns = [
    path('genre/', detail_genre_view, name="details_genre"),
    path('account_genre/create', create_account_genre_view, name="create_account_genre"),
    path('song/create/', create_song_view, name="create_song"),
    path('song/', detail_song_view, name="details_song"),
    path('song/update/', update_song_view, name="update_song"),
    path('song/delete/', delete_song_view, name="delete_song"),
]