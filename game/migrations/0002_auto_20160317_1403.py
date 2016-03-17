# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='creator',
            field=models.ForeignKey(to='user_profile.Profile'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_accepted',
            field=models.ForeignKey(related_name='team_accepted', blank=True, to='user_profile.Profile', null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='team_creator',
            field=models.ForeignKey(related_name='team_creator', to='user_profile.Profile'),
        ),
    ]
