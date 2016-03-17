# -*- coding: utf-8 -*-
from django import forms
from game.models import Game

from kids_football.widgets import DateTimePickerWidget


class CreateGameForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateGameForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Game
        fields = ['title', 'date_time_start', 'type', 'location', 'duration', 'age']
        widgets = {
            'date_time_start': DateTimePickerWidget()
        }