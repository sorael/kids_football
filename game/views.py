from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from game.models import Game
from game.forms import CreateGameForm


def index(request, page=1):
    all_games = Paginator(Game.objects.all().select_related(
        'team_creator', 'team_accepted', 'creator__user'), 5)
    return render(request, 'game/index.html',
                  {'all_games': all_games.page(page)})


@login_required
def create_game(request):
    create_game_form = CreateGameForm()
    # user = request.user
    # profile, created = Profile.objects.get_or_create(user=user)
    # edit_profile_form = ProfileEditForm(instance=profile)
    # edit_user_form = UserEditForm(instance=user)
    # # game = Game.objects.create()
    return render(request, 'game/create_game.html',
                  {'create_game_form': create_game_form})