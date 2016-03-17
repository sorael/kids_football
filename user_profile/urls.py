# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^edit$', 'user_profile.views.edit_profile', name='edit_profile'),

)
