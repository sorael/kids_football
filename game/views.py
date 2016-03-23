import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator

from game.models import Game
from user_profile.models import Profile
from game.forms import CreateGameForm


def index(request, page=1):
    games = Paginator(Game.objects.all().select_related('creator__user'), 5)
    return render(request, 'game/index.html',
                  {'games': games.page(page)})


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
