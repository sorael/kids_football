# -*- coding: utf-8
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from user_profile.fields import AutoOneToOneField
# from team.models import Team


# class Profile(models.Model):
#     user = AutoOneToOneField(User, related_name='profile', primary_key=True,
#                              verbose_name='User')
#     team = models.ForeignKey(Team, blank=True, verbose_name='Команда')
#     date_of_birth = models.DateField(blank=True, verbose_name='Дата рождения')
#     photo = models.ImageField(upload_to='photos', blank=True, null=True,
#                               verbose_name='Аватарка')
#
#     def save(self, *args, **kwargs):
#         super(Profile, self).save(*args, **kwargs)
#         if self.photo:
#             image = Image.open(self.photo)
#             image.thumbnail((150, 150), Image.ANTIALIAS)
#             image.save(self.photo.path, 'JPEG', quality=80)
#
#     class Meta:
#         verbose_name = 'профиль'
#         verbose_name_plural = 'профили'


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', primary_key=True,
                                verbose_name='User')
    team = models.CharField(max_length=250, blank=True, null=True, verbose_name='Команда')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='photos', blank=True, null=True,
                              verbose_name='Аватарка')

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if self.photo:
            image = Image.open(self.photo)
            image.thumbnail((150, 150), Image.ANTIALIAS)
            image.save(self.photo.path, 'JPEG', quality=80)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'