# -*- coding: utf-8 -*-
from django.db import models
from user_profile.models import Profile


AGE = (('a5a7', 'от 5 до 7'),
       ('a7a9', 'от 7 до 9'),
       ('a9a11', 'от 9 до 11'),
       ('a11a13', 'от 11 до 13'),
       ('a13a15', 'от 13 до 15'),)

TYPES = (('friend', 'товарищеская игра'),
         ('tournament', 'турнир'),
         ('training', 'тренировка'),)


class Game(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250)
    team_creator = models.CharField(max_length=250)
    team_accepted = models.CharField(max_length=250, blank=True, null=True)
    date_time_start = models.DateTimeField(verbose_name='Дата, время начала')
    type = models.CharField(max_length=15, choices=TYPES,
                            verbose_name='Тип игры')
    location = models.TextField(verbose_name='Где будем играть')
    duration = models.CharField(max_length=250, verbose_name='Длительность')
    age = models.CharField(max_length=6, choices=AGE,
                           verbose_name='Возрастная категория')
    creator = models.ForeignKey(Profile)
    winner = models.NullBooleanField(blank=True, null=True)
    score = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'игра'
        verbose_name_plural = 'игры'