# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('slug', models.SlugField(max_length=250)),
                ('team_creator', models.CharField(max_length=250)),
                ('team_accepted', models.CharField(max_length=250, null=True, blank=True)),
                ('date_time_start', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0, \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0')),
                ('type', models.CharField(max_length=15, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb8\xd0\xb3\xd1\x80\xd1\x8b', choices=[(b'friend', b'\xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd0\xb8\xd1\x89\xd0\xb5\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f \xd0\xb8\xd0\xb3\xd1\x80\xd0\xb0'), (b'tournament', b'\xd1\x82\xd1\x83\xd1\x80\xd0\xbd\xd0\xb8\xd1\x80'), (b'training', b'\xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0')])),
                ('location', models.TextField(verbose_name=b'\xd0\x93\xd0\xb4\xd0\xb5 \xd0\xb1\xd1\x83\xd0\xb4\xd0\xb5\xd0\xbc \xd0\xb8\xd0\xb3\xd1\x80\xd0\xb0\xd1\x82\xd1\x8c')),
                ('duration', models.CharField(max_length=250, verbose_name=b'\xd0\x94\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('age', models.CharField(max_length=6, verbose_name=b'\xd0\x92\xd0\xbe\xd0\xb7\xd1\x80\xd0\xb0\xd1\x81\xd1\x82\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', choices=[(b'a5a7', b'\xd0\xbe\xd1\x82 5 \xd0\xb4\xd0\xbe 7'), (b'a7a9', b'\xd0\xbe\xd1\x82 7 \xd0\xb4\xd0\xbe 9'), (b'a9a11', b'\xd0\xbe\xd1\x82 9 \xd0\xb4\xd0\xbe 11'), (b'a11a13', b'\xd0\xbe\xd1\x82 11 \xd0\xb4\xd0\xbe 13'), (b'a13a15', b'\xd0\xbe\xd1\x82 13 \xd0\xb4\xd0\xbe 15')])),
                ('winner', models.NullBooleanField()),
                ('score', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u0438\u0433\u0440\u0430',
                'verbose_name_plural': '\u0438\u0433\u0440\u044b',
            },
        ),
    ]
