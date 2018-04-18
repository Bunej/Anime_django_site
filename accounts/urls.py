from django.urls import path, re_path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    re_path(r'^profile/(?P<username>\w+)/$', views.profile_view, name="profile"),
    path('profile/edit', views.edit_profile, name="edit_profile"),
    path('change-password', views.change_password, name="change_password"),
]
