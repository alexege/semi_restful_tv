from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows/new$', views.new_shows),
    url(r'^shows/create$', views.shows_create),
    url(r'^shows/(?P<id>\d+)$', views.show_description),
    url(r'^delete$', views.delete_database),
    url(r'^shows/(?P<id>\d+)/edit$', views.show_id_edit),
    url(r'^shows/(?P<id>\d+)/update$', views.show_id_update),
    url(r'^shows/(?P<id>\d+)/delete$', views.show_id_delete),
]

#index: views.index
#shows/new: views.new_shows
#shows/create: views.shows_create