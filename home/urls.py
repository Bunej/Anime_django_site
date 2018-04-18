from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^episode/(?P<slug>[\w-]+)/$', views.anime_title, name='anime_title'),
    re_path(r'^episode/(?P<slug>[\w-]+)/comment/$', views.add_comment, name='add_comment')
]
