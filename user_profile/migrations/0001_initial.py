# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(related_name='profile', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name=b'User')),
                ('team', models.CharField(max_length=250, null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0', blank=True)),
                ('date_of_birth', models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('photo', models.ImageField(upload_to=b'photos', null=True, verbose_name=b'\xd0\x90\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80\xd0\xba\xd0\xb0', blank=True)),
            ],
            options={
                'verbose_name': '\u043f\u0440\u043e\u0444\u0438\u043b\u044c',
                'verbose_name_plural': '\u043f\u0440\u043e\u0444\u0438\u043b\u0438',
            },
        ),
    ]
