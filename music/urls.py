from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/2
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add
    url(r'album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/update
    url(r'^album/(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/register/
    url(r'^register/$', views.UserFormView.as_view(), name='user-register'),

# /music/login/
    url(r'^login/$', views.LoginView.as_view(), name='user-login'),

# /music/logout/
    url(r'^logout/$', views.logoutView, name='user-logout')
]