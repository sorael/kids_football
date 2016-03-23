# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'game.views.index', name='index'),
    url(r'^create_game/', 'game.views.create_game', name='create_game'),
    url(r'^my_games/', 'game.views.my_games', name='my_games'),
    url(r'^edit_game/(?P<game_id>\d+)/$', 'game.views.edit_game', name='edit_game'),

)
