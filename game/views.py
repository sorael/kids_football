import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator

from game.models import Game
from user_profile.models import Profile
from game.forms import CreateGameForm


def index(request, page=1):
    try:
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
    except TypeError:
        profile = None
    games = Paginator(Game.objects.all().select_related('creator__user'), 5)
    return render(request, 'game/index.html',
                  {'games': games.page(page),
                   'profile': profile})


@login_required
def create_game(request):
    response = {}
    user = request.user
    profile, create = Profile.objects.get_or_create(user=user)
    if request.POST:
        create_game_form = CreateGameForm(request.POST)
        if create_game_form.is_valid():
            game = create_game_form.save(commit=False)
            game.team_creator = profile.team
            game.creator = profile
            game.save()
            response['success'] = 'true'
            return HttpResponse(json.dumps(response),
                                content_type='application/json')
        else:
            if create_game_form.errors:
                errs = {}
                for error in create_game_form.errors:
                    e = create_game_form.errors[error]
                    errs[error] = unicode(e)
                response['success'] = 'false'
                response['errors'] = errs
            return HttpResponse(json.dumps(response),
                                content_type='application/json')
    return render(request, 'game/create_game.html',
                  {'create_game_form': CreateGameForm(),
                   'profile': profile})


@login_required
def edit_game(request, game_id):
    user = request.user
    game = Game.objects.select_related('creator').get(id=game_id)
    if user == game.creator.user:
        profile = Profile.objects.get(user=user)
        response = {}
        if request.POST and request.is_ajax():
            edit_game_form = CreateGameForm(request.POST, instance=game)
            if edit_game_form.is_valid():
                edit_game_form.save()
                response['success'] = 'true'
                return HttpResponse(json.dumps(response),
                                    content_type='application/json')
            else:
                if edit_game_form.errors:
                    errs = {}
                    for error in edit_game_form.errors:
                        e = edit_game_form.errors[error]
                        errs[error] = unicode(e)
                    response['success'] = 'false'
                    response['errors'] = errs
                return HttpResponse(json.dumps(response),
                                    content_type='application/json')
        return render(request, 'game/edit_game.html',
                      {'edit_game_form': CreateGameForm(instance=game),
                       'profile': profile,
                       'game': game})
    else:
        return render(request, 'game/edit_game.html',
                      {'access_denied': 'access_denied'})



@login_required
def my_games(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    games = Game.objects.all().select_related('creator__user').filter(creator=profile)
    return render(request, 'game/index.html',
                  {'games': games,
                   'profile': profile})
