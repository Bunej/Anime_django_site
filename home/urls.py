from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^episode/(?P<slug>[\w-]+)/$', views.anime_title, name='anime_title'),
    re_path(r'^episode/(?P<slug>[\w-]+)/comment/$', views.add_comment, name='add_comment'),
    re_path(r'^episode/(?P<slug>[\w-]+)/edit/(?P<id>\d+)/?', views.edit_comment, name='edit_comment'),
    re_path(r'^episode/(?P<slug>[\w-]+)/delete/(?P<id>\d+)/?', views.delete_comment, name='delete_comment'),
    path('add_anime/', views.add_anime, name='add_anime'),
    path('add_episode/', views.add_episode, name='add_episode'),
]
