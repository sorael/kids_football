# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'game.views.index', name='index'),
    url(r'^create_game/', 'game.views.create_game', name='create_game'),

)
