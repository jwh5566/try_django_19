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
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^$', post_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),

]
