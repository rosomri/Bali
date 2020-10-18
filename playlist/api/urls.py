from django.urls import path
from playlist.api.views import (
    detail_genre_view,
    detail_song_view,
    delete_song_view,
    update_song_view,
    create_song_view
)
app_name = "playlist"

urlpatterns = [
    path('genre/<title>/', detail_genre_view, name="details_genre"),
    path('song/<id>/', detail_song_view, name="details_song"),
    path('song/create/', create_song_view, name="create_song"),
    path('song/<id>/update/', update_song_view, name="update_song"),
    path('song/<id>/delete/', delete_song_view, name="delete_song"),
]