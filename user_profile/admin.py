from django.contrib import admin
from user_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'date_of_birth', 'photo']
