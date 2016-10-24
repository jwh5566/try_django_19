# -*- coding: utf-8 -*-
__author__ = 'Administrator'

from django.conf.urls import url
from .views import (
    post_create,
    post_update,
    post_list,
    post_detail,
    post_delete
)

urlpatterns = [
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^$', post_list, name="list"),
    url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
    url(r'^(?P<id>\d+)/delete/$', post_delete),

]
