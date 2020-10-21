from django.urls import path
from playlist.api.views import (
    detail_genre_view,
    detail_song_view,
    delete_song_view,
    update_song_view,
    create_song_view,
    create_account_genre_view,
    ApiAccountSongListView,
    ApiGenreListView,
    ApiAccountGenreListView,
    ApiOptionalSongList,
    update_song_data
)
app_name = "playlist"

urlpatterns = [
    path('genre/', detail_genre_view, name="details_genre"),
    path('genre/list/', ApiGenreListView.as_view(), name="all_genre_list"),
    path('song/', detail_song_view, name="details_song"),
    path('song/create/', create_song_view, name="create_song"),
    path('song/update/', update_song_view, name="update_song"),
    path('song/delete/', delete_song_view, name="delete_song"),
    path('account_songs/', ApiAccountSongListView.as_view(), name="account_songs_list"),
    path('optional_songs/<username>/', ApiOptionalSongList.as_view(), name="all_optional_songs"),
    path('account_genre/list/', ApiAccountGenreListView.as_view(), name="account_genre_list"),
    path('account_genre/create/', create_account_genre_view, name="create_account_genre"),
    # temp url for song data update
    path('song/update_data/', update_song_data, name="update_songs_data"),
    # path('callback/')
]