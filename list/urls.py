from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.list, name='list'),
    re_path(r'^(?P<letter>[A-Z]{1})/', views.list_detail, name='list_detail'),
    path('ended/', views.ended, name='ended'),

]
