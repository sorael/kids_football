# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from user_profile.models import Profile
from user_profile.forms import ProfileEditForm, UserEditForm


@login_required
def edit_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    edit_profile_form = ProfileEditForm(instance=profile)
    edit_user_form = UserEditForm(instance=user)
    if request.POST:
        edit_profile_form = ProfileEditForm(request.POST, request.FILES,
                                            instance=profile)
        edit_user_form = UserEditForm(request.POST, instance=user)
        if edit_profile_form.is_valid() and edit_user_form.is_valid():
            user_form = edit_user_form.save()
            profile = edit_profile_form.save(commit=False)
            profile.user = user_form
            profile.save()
            return redirect('index')
    return render(request, 'user_profile/edit_profile.html',
                  {'edit_profile_form': edit_profile_form,
                   'form': edit_profile_form,
                   'edit_user_form': edit_user_form,
                   'profile': profile})
