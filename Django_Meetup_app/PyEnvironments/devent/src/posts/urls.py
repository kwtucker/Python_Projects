from django.conf.urls import url
from django.contrib import admin
# importing the functions from the views so the url call them.
from .views import (
                    event_list,
                    event_create,
                    event_comment_update,
                    event_delete,
                    get,
                    event_comment,
                    )
urlpatterns = [
    url(r'^$', event_list, name='list'),
    url(r'^create/$', event_create),
    url(r'^(?P<id>\d+)/edit/$', event_comment_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', event_delete),
    url(r'^get/$', get, name='get'),
    url(r'^edit/(?P<id>\d+)/$', event_comment, name='comment'),
]
