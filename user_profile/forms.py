# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

from user_profile.models import Profile
from kids_football.widgets import DatePickerWidget


class ProfileEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['photo', 'date_of_birth']:
                self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['team', 'date_of_birth', 'photo']
        widgets = {
            'date_of_birth': DatePickerWidget(
                attrs={'class': 'form-control datepicker-here',
                       'readonly': 'readonly'}),
            'photo': forms.FileInput()
        }


class UserEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
