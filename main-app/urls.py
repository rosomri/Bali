from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    # gnum is the parameter which tells the index of genre
    url(r'^genres/', views.choose_genres, name='genres'),
    # path('<str:username>/', views.user, name='user'),
]