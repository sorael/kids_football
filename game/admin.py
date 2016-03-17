from django.contrib import admin
from game.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'date_time_start', 'type', 'location',
                    'duration', 'age', 'creator', 'winner', 'score']
    prepopulated_fields = {'slug': ('title',)}
